#! /usr/bin/env python3
import copy
import rospy
import signal
from threading import Thread
from tf import transformations
from tf2_geometry_msgs import PoseStamped
from mavros_msgs.msg import AttitudeTarget, State
from mavros_msgs.srv import CommandBool, SetMode, SetModeRequest
import numpy as np
from drone_controller.srv import TakeOff, Land, GoToPoint, GoHome
from visualization_msgs.msg import Marker
from utils import LowPassFilter, MAFilter
import time
import tf2_ros as tf2
from dynamic_reconfigure.server import Server
from drone_controller.cfg import ParamsConfig
from drone_pid import DronePid
from drone_lqr import DroneLQR
from drone_lqr_new import NewDroneLQR
from scipy.spatial.transform import Rotation as R
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue

from scipy import io as sio


class Controller:
    def __init__(self):
        self.drone_states = {
            "GROUND": 0,
            "TAKING_OFF": 1,
            "FLYING": 2,
            "LANDING": 3,
            "FAIL": 4
        }
        self.current_state = self.drone_states["GROUND"]
        self.takeoff_thr = 0.05
        self.landing_thr = 0.05

        # inputs
        self.controller_roll = np.array([])
        self.controller_pitch = np.array([])
        self.controller_yaw = np.array([])
        self.controller_thrust = np.array([])

        # outputs
        self.pose_x = np.array([])
        self.pose_y = np.array([])
        self.pose_z = np.array([])

        self.time_data = np.array([])

        # Node Initialization
        rospy.init_node("drone_controller", anonymous=False)
        global_name = "/drone_controller"

        # Parameter Server
        self.params_server = Server(ParamsConfig, self.params_callback)

        # Control Z
        self.trust_as_trust = rospy.get_param("{}/trust_as_trust".format(global_name))

        # Controller
        self.fs = rospy.get_param("{}/fs".format(global_name))
        self.dt = 1 / self.fs
        self.tc = rospy.get_param("{}/Tc".format(global_name))
        self.angle_mode = rospy.get_param("{}/angle_mode".format(global_name))
        self.exp_acrobatic_model = rospy.get_param("{}/exp_acrobatic_model".format(global_name))
        self.world_frame = rospy.get_param("{}/world_frame".format(global_name))
        self.drone_frame = rospy.get_param("{}/drone_frame".format(global_name))

        # Safety Space
        self.room_min_x = rospy.get_param("{}/room_min_x".format(global_name))
        self.room_max_x = rospy.get_param("{}/room_max_x".format(global_name))
        self.room_min_y = rospy.get_param("{}/room_min_y".format(global_name))
        self.room_max_y = rospy.get_param("{}/room_max_y".format(global_name))
        self.room_min_z = rospy.get_param("{}/room_min_z".format(global_name))
        self.room_max_z = rospy.get_param("{}/room_max_z".format(global_name))

        # Control Policy
        self.controller = DronePid(trust_as_trust=self.trust_as_trust)
        if self.exp_acrobatic_model:
            self.controller_lqr = NewDroneLQR()
        else:
            self.controller_lqr = DroneLQR()

        # Exit policy
        rospy.on_shutdown(self.stop_node)

        # Rates
        self.rate_fsm_diagnostic = rospy.Rate(20)
        self.rate_pid = rospy.Rate(self.fs)
        self.rate_pose = rospy.Rate(self.fs * 1.2)

        # Service to ARM/DISARM the Drone and to set the flight Mode
        rospy.wait_for_service("/mavros/cmd/arming")
        self.arming_service = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)

        rospy.wait_for_service("/mavros/set_mode")
        self.mode_service = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        self.OFF_BOARD_MODE = "GUIDED"

        # Interaction
        self.takeoff_service = rospy.Service("{}/take_off".format(global_name), TakeOff, self.take_off)
        self.go_to_point_service = rospy.Service("{}/go_to_point".format(global_name), GoToPoint, self.go_to_point_srv)
        self.land_service = rospy.Service("{}/land".format(global_name), Land, self.land)
        self.home_service = rospy.Service("{}/go_home".format(global_name), GoHome, self.go_home)
        self.set_point_subscriber = rospy.Subscriber("{}/goal".format(global_name), PoseStamped, self.go_to_point,
                                                     queue_size=10)
        self.fcu_set_point_publisher = rospy.Publisher('/mavros/setpoint_raw/attitude', AttitudeTarget, queue_size=1)
        self.guid_set_point_publisher = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=1)
        self.diagnostic_publisher = rospy.Publisher("/drone_controller/diagnostics", DiagnosticArray, queue_size=10)

        # Visualization
        self.visualization_publisher = rospy.Publisher("{}/visualization".format(global_name), Marker, queue_size=100)

        # Transforms
        self.tf_buffer = tf2.Buffer()
        self.tf_listener = tf2.TransformListener(self.tf_buffer)

        try:
            transform = self.tf_buffer.lookup_transform(self.world_frame, self.drone_frame, rospy.Time(0),
                                                        rospy.Duration(5))
        except tf2.LookupException:
            print("ERROR: No transformation between {} and {}. Cannot initialize the node. Exiting...".format(
                self.drone_frame, self.world_frame))
            exit(-1)

        self.init_pose = np.array([transform.transform.translation.x,
                                   transform.transform.translation.y,
                                   transform.transform.translation.z])
        quaternion = np.array([transform.transform.rotation.x,
                               transform.transform.rotation.y,
                               transform.transform.rotation.z,
                               transform.transform.rotation.w])
        _, _, init_yaw = transformations.euler_from_quaternion(quaternion)
        self.init_yaw = np.array([init_yaw])

        self.current_pose = copy.deepcopy(self.init_pose)
        self.current_orientation = copy.deepcopy(quaternion)

        self.set_point = copy.deepcopy(self.init_pose)
        self.set_point_yaw = copy.deepcopy(self.init_yaw)
        self.home = copy.deepcopy(self.init_pose)
        self.home_yaw = copy.deepcopy(self.init_yaw)
        self.takeoff_altitude = 0.0

        # Filter Ref Signal
        self.ma_filter = MAFilter(np.concatenate([self.init_pose, self.init_yaw]), self.tc, self.dt)
        self.low_pass_filter = LowPassFilter(np.concatenate([self.init_pose, self.init_yaw]), self.tc / 4, self.dt)

        # Check Room Bounds
        self.room_min_z = self.init_pose[
            2]  # DA RIGUARDARE, QUI INIZIALIZZO LA Z MINIMA CON LA POSA CORRENTE E IGNORO QUELLA DEI SETTINGS
        if not self._check_room():
            print("ERROR: The Room shape is incorrect. Current Values:")
            print("room_min_x: {}".format(self.room_min_x))
            print("room_max_x: {}".format(self.room_max_x))
            print("room_min_y: {}".format(self.room_min_y))
            print("room_max_y: {}".format(self.room_max_y))
            print("room_min_z: {}".format(self.room_min_z))
            print("room_max_z: {}".format(self.room_max_z))
            exit(-1)
        if not self._check_point_in_room(self.init_pose[0], self.init_pose[1], self.init_pose[2]):
            print("ERROR: The Drone is outside the Room")
            print("Drone position: {}".format(self.init_pose))
            print("room_min_x: {}".format(self.room_min_x))
            print("room_max_x: {}".format(self.room_max_x))
            print("room_min_y: {}".format(self.room_min_y))
            print("room_max_y: {}".format(self.room_max_y))
            print("room_min_z: {}".format(self.room_min_z))
            print("room_max_z: {}".format(self.room_max_z))
            exit(-1)

        # Logs
        self.errors = {"error_pitch": 0.0,
                       "error_roll": 0.0,
                       "error_trust": 0.0}
        self.pid_remapped = {"pitch": 0.0,
                             "roll": 0.0,
                             "trust": 0.0}
        self.pitch_components = {"p": 0.0,
                                 "i": 0.0,
                                 "d": 0.0}
        self.roll_components = {"p": 0.0,
                                "i": 0.0,
                                "d": 0.0}
        self.trust_components = {"p": 0.0,
                                 "i": 0.0,
                                 "d": 0.0}

        # Threads
        self.last_time = time.monotonic()
        self.control_pitch_roll = True
        self.kill_threads = False
        self.pid_thread = Thread(target=self._control_loop)
        self.update_pose_thread = Thread(target=self._update_pose_loop)

        self.pid_thread.start()
        self.update_pose_thread.start()

        # shutdown
        signal.signal(signal.SIGINT, self._handler_sigint)

    def _check_point_in_room(self, x, y, z):
        result = True
        if x > self.room_max_x or x < self.room_min_x:
            result = False
        if y > self.room_max_y or y < self.room_min_y:
            result = False
        if z > self.room_max_z or z < self.room_min_z:
            result = False
        return result

    def _check_home(self):
        result = False
        if abs(self.current_pose[0] - self.home[0]) < 0.1 \
                and abs(self.current_pose[1] - self.home[1]) < 0.1 \
                and abs(self.current_pose[2] - (self.home[2] + self.takeoff_altitude)) < 0.1:
            result = True
        return result

    def _check_room(self):
        result = True
        if self.room_max_x <= self.room_min_x:
            result = False
        if self.room_max_y <= self.room_min_y:
            result = False
        if self.room_max_z <= self.room_min_z:
            result = False
        return result

    def _update_pose_loop(self):
        while not self.kill_threads:
            try:
                transform = self.tf_buffer.lookup_transform(self.world_frame, self.drone_frame, rospy.Time(0))
                self.current_pose = np.array([transform.transform.translation.x,
                                              transform.transform.translation.y,
                                              transform.transform.translation.z])
                self.current_orientation = np.array([transform.transform.rotation.x,
                                                     transform.transform.rotation.y,
                                                     transform.transform.rotation.z,
                                                     transform.transform.rotation.w])
            except tf2.LookupException:
                print("ERROR: No TF available between {} and {}.".format(self.world_frame, self.drone_frame))

            self.rate_pose.sleep()

    def take_off(self, data):
        result = False
        altitude = data.altitude

        # Check a reasonable value for taking off
        if not (altitude > 0.2 and altitude < 1.0):  ## BRUTTOOOOO
            altitude = 0.4

        if self.current_state == self.drone_states["GROUND"]:
            point = PoseStamped()
            point.header.stamp = rospy.Time.now()
            point.header.frame_id = self.drone_frame
            point.pose.position.z = altitude
            point.pose.orientation.w = 1

            result = self.update_set_point(point)

            if result:
                current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(2))
                if current_state.mode != "GUIDED":
                    print("primo if: " + current_state.mode)
                    offb_set_mode = SetModeRequest()
                    offb_set_mode.custom_mode = "GUIDED"
                    self.mode_service.call(offb_set_mode)
                    time.sleep(3.0)
                    current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(2))
                    if current_state.mode != "GUIDED":
                        print("secondo if: " + current_state.mode)
                        rospy.loginfo("Cannot set mode GUIDED")
                        return False
                start_timer = time.time()

                # Wait Arming from remote
                armed = False
                while not (armed and start_timer + 15.0 > time.time()):
                    try:
                        self.arming_service.call(value=True)  # Use ONLY on Gazebo Simulation
                        current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(2))
                        armed = current_state.armed
                    except AttributeError:
                        print("AttributeError: maybe the connection has been lost??")
                if not armed:
                    rospy.loginfo("Drone not armed")
                    return False
            else:
                print("TAKE OFF ERROR!")
                return False
            time.sleep(3)
            self.current_state = self.drone_states["TAKING_OFF"]
            self.takeoff_altitude = altitude
        return result

    def params_callback(self, config, level):
        return config

    def _handler_sigint(self, signum, frame):
        self.stop_node()

    def stop_node(self):
        #print("current state: {}".format(self.current_state))
        if self.current_state == self.drone_states["TAKING_OFF"] or self.current_state == self.drone_states["FLYING"]:
            self.land(0)
        while not self.current_state == self.drone_states["GROUND"]:
            #print("enter stopping")
            self.diagnostic_loop()
            #print("after diagn")
            self.fsm_loop()
            #print("after loop")
            self.sleep()
            #print("after sleep")
            self.kill_threads = True
        #print("alibaba")

    def _control_loop(self):
        while not self.kill_threads:
            current_pose = self.current_pose
            current_orientation = self.current_orientation
            _, _, current_yaw = transformations.euler_from_quaternion(current_orientation)
            r = R.from_quat(current_orientation)
            current_rotation_matrix = np.array(r.as_matrix()).reshape((3, 3))
            if self.current_state != self.drone_states["GROUND"]:
                # Smoothing the set point and calculating the error
                set_point_smooth = self.low_pass_filter.filter(
                    self.ma_filter.filter(np.concatenate([self.set_point, self.set_point_yaw])))
                des_pose = set_point_smooth[:3]
                des_yaw = set_point_smooth[3]
                current_error_yaw = des_yaw - current_yaw
                current_error = des_pose - current_pose

                xp = np.append(self.pose_x, [current_pose[0]])
                self.pose_x = xp

                yp = np.append(self.pose_y, [current_pose[1]])
                self.pose_y = yp

                zp = np.append(self.pose_z, [current_pose[2]])
                self.pose_z = zp

                tapp = np.append(self.time_data, [time.time()])
                self.time_data = tapp

                print("[{}] {}".format(time.time(), current_pose.flatten()))

                error_x, error_y, error_z = current_error

                # Log
                pitch, roll, trust, yaw = 0, 0, 0, 0
                pitch_p, pitch_i, pitch_d = 0, 0, 0
                roll_p, roll_i, roll_d = 0, 0, 0
                trust_p, trust_i, trust_d = 0, 0, 0

                if not self.current_state == self.drone_states["FAIL"]:
                    if not self.current_state == self.drone_states["TAKING_OFF"] and self.control_pitch_roll:
                        if self.angle_mode:
                            rotation_matrix = np.array([[np.cos(current_yaw), -np.sin(current_yaw)],
                                                        [np.sin(current_yaw), np.cos(current_yaw)]]).transpose()

                            error_matrix = np.array([[error_x, error_y]]).transpose()

                            rotated_error_x, rotated_error_y = np.dot(rotation_matrix, error_matrix).flatten()

                            pitch = self.controller.pitch(rotated_error_x)
                            roll = self.controller.roll(rotated_error_y)
                            yaw = des_yaw
                            trust = self.controller.trust(error_z, mes=current_pose[2])

                            r1 = np.append(self.controller_roll, [roll])
                            self.controller_roll = r1

                            p1 = np.append(self.controller_pitch, [pitch])
                            self.controller_pitch = p1

                            y1 = np.append(self.controller_yaw, [yaw])
                            self.controller_yaw = y1

                            t1 = np.append(self.controller_thrust, [trust])
                            self.controller_thrust = t1

                            self.publish_attitude_angle(pitch=pitch, roll=roll, yaw=yaw, trust=trust)

                            # Log
                            error_x = rotated_error_x
                            error_y = rotated_error_y
                            pitch_p, pitch_i, pitch_d = self.controller.pitch_components
                            roll_p, roll_i, roll_d = self.controller.roll_components
                            trust_p, trust_i, trust_d = self.controller.trust_components
                        else:
                            lqr_observation = {"p": current_error.reshape((1, 3)),
                                               "R": current_rotation_matrix,
                                               "yaw": current_error_yaw}
                            wtr, trust = self.controller_lqr.perform_action(lqr_observation)
                            self.publish_attitude_acro(wtr[0], wtr[1], wtr[2], trust)
                    else:
                        pitch = self.controller.default_pitch
                        roll = self.controller.default_roll
                        yaw = self.init_yaw[0]
                        if self.angle_mode:
                            if self.trust_as_trust:
                                trust = self.controller.trust(error_z, mes=current_pose[2])
                            else:
                                trust = self.controller.TRUST_STATIC_CLIMB * 1.2
                        else:
                            lqr_observation = {"p": current_error.reshape((1, 3)),
                                               "R": current_rotation_matrix,
                                               "yaw": np.array([0.0])}
                            _, trust = self.controller_lqr.perform_action(lqr_observation)

                        r2 = np.append(self.controller_roll, [roll])
                        self.controller_roll = r2

                        p2 = np.append(self.controller_pitch, [pitch])
                        self.controller_pitch = p2

                        y2 = np.append(self.controller_yaw, [yaw])
                        self.controller_yaw = y2

                        t2 = np.append(self.controller_thrust, [trust])
                        self.controller_thrust = t2

                        self.publish_attitude_angle(pitch=pitch, roll=roll, yaw=yaw, trust=trust)
                else:
                    self.publish_guided_setpoint(des_pose[0], des_pose[1], des_pose[2], des_yaw)

                # Logs
                self.errors = {"error_pitch": error_x,
                               "error_roll": error_y,
                               "error_trust": error_z}
                self.pid_remapped = {"pitch": pitch,
                                     "roll": roll,
                                     "trust": trust}
                self.pitch_components = {"p": pitch_p,
                                         "i": pitch_i,
                                         "d": pitch_d}
                self.roll_components = {"p": roll_p,
                                        "i": roll_i,
                                        "d": roll_d}
                self.trust_components = {"p": trust_p,
                                         "i": trust_i,
                                         "d": trust_d}

            input_output_dic = {
                "controller_roll": self.controller_roll,
                "controller_pitch": self.controller_pitch,
                "controller_yaw": self.controller_yaw,
                "controller_thrust": self.controller_thrust,
                "pose_x": self.pose_x,
                "pose_y": self.pose_y,
                "pose_z": self.pose_z,
                "time": self.time_data
            }

            sio.savemat("input_output_data.mat", input_output_dic)

            self.rate_pid.sleep()

        print("end control loop")


    def diagnostic_loop(self):
        # Diagnostics
        set_point_smooth = self.low_pass_filter.state
        des_pose = set_point_smooth[:3]
        des_yaw = set_point_smooth[3]
        current_roll, current_pitch, current_yaw = transformations.euler_from_quaternion(self.current_orientation)
        log = {
            "ts": rospy.Time.now(),
            "status": self.current_state,
            "x": self.current_pose[0],
            "y": self.current_pose[1],
            "z": self.current_pose[2],
            "pitch": current_roll,
            "roll": current_pitch,
            "yaw": current_yaw,
            "set_point_x_smooth": des_pose[0],
            "set_point_y_smooth": des_pose[1],
            "set_point_z_smooth": des_pose[2],
            "set_point_yaw_smooth": des_yaw,
            "set_point_x": self.set_point[0],
            "set_point_y": self.set_point[1],
            "set_point_z": self.set_point[2],
            "set_point_yaw": self.set_point_yaw[0],
            "error_pitch": self.errors['error_pitch'],
            "error_roll": self.errors['error_roll'],
            "error_trust": self.errors['error_trust'],
            "PID_pitch": self.controller.pitch_last_output,
            "PID_roll": self.controller.roll_last_output,
            "PID_trust": self.controller.trust_last_output,
            "PID_pitch_remapped": self.pid_remapped['pitch'],
            "PID_roll_remapped": self.pid_remapped['roll'],
            "PID_trust_remapped": self.pid_remapped['trust'],
            "PID_pitch_p": self.pitch_components['p'],
            "PID_pitch_i": self.pitch_components['i'],
            "PID_pitch_d": self.pitch_components['d'],
            "PID_roll_p": self.roll_components['p'],
            "PID_roll_i": self.roll_components['i'],
            "PID_roll_d": self.roll_components['d'],
            "PID_trust_p": self.trust_components['p'],
            "PID_trust_i": self.trust_components['i'],
            "PID_trust_d": self.trust_components['d']
        }
        self.publish_diagnostics(log)

    def fsm_loop(self):
        # FSM Check, Safety and R-VIZ Visualization
        if self.current_state == self.drone_states["TAKING_OFF"]:
            if abs(self.current_pose[2] - self.init_pose[2]) > self.takeoff_thr:
                self.reset_pitch_roll_yaw()
                self.current_state = self.drone_states["FLYING"]
        if self.current_state == self.drone_states["LANDING"]:
            current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(1))
            if not current_state.armed:
                self.current_state = self.drone_states["GROUND"]
                _, _, current_yaw = transformations.euler_from_quaternion(self.current_orientation)
                self.ma_filter = MAFilter(np.concatenate([self.current_pose, np.array([current_yaw])]), self.tc,
                                          self.dt)
                self.low_pass_filter = LowPassFilter(np.concatenate([self.current_pose, np.array([current_yaw])]),
                                                     self.tc / 4, self.dt)
                self.set_point = self.current_pose
                self.set_point_yaw = np.array([current_yaw])
                self.controller.reset()

        # Safety Check
        if self.current_state == self.drone_states["FLYING"] and not self._check_point_in_room(self.current_pose[0],
                                                                                               self.current_pose[1],
                                                                                               self.current_pose[2]):
            self.go_home(None)
            self.current_state = self.drone_states["FAIL"]

        if self.current_state == self.drone_states["FAIL"]:
            if self._check_home() and self._check_point_in_room(self.current_pose[0],
                                                                self.current_pose[1],
                                                                self.current_pose[2]):
                current_time = time.monotonic()
                if current_time - self.last_time > 2.0:
                    self.land(None)
            else:
                self.last_time = time.monotonic()

        # Visualization
        set_point_smooth = self.low_pass_filter.state
        des_pose = set_point_smooth[:3]
        des_yaw = set_point_smooth[3]
        self._publish_safety_room()
        self._publish_point(self.set_point, 0, yaw=self.set_point_yaw[0])
        self._publish_point(des_pose, 1, yaw=des_yaw, g=0.0, b=1.0)

    def land(self, data):
        result = False
        if self.current_state != self.drone_states["GROUND"] and self.current_state != self.drone_states["LANDING"]:
            start_time = time.time()
            landing = False
            while not landing and time.time() - start_time < 10.0:
                land_set_mode = SetModeRequest()
                land_set_mode.custom_mode = 'LAND'
                ack = self.mode_service.call(land_set_mode).mode_sent
                current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(1))
                if current_state.mode == 'LAND':
                    landing = True
                    result = True

            self.current_state = self.drone_states["LANDING"]
        return result

    def go_to_point_srv(self, data):
        point = data.pose
        return self.go_to_point(point)

    def go_to_point(self, data):
        result = False
        if self.current_state == self.drone_states["FLYING"]:
            frame = data.header.frame_id
            x = data.pose.position.x
            y = data.pose.position.y
            z = data.pose.position.z
            qx = data.pose.orientation.x
            qy = data.pose.orientation.y
            qz = data.pose.orientation.z
            qw = data.pose.orientation.w

            # if not (frame == self.drone_frame or frame == self.world_frame):  # Da controllare, forse non serve
                # return False

            point = PoseStamped()
            point.header.frame_id = frame
            point.pose.position.x = x
            point.pose.position.y = y
            point.pose.position.z = z
            point.pose.orientation.x = qx
            point.pose.orientation.y = qy
            point.pose.orientation.z = qz
            point.pose.orientation.w = qw

            result = self.update_set_point(point)

        return result

    def sleep(self):
        self.rate_fsm_diagnostic.sleep()

    def update_set_point(self, data):
        result = False
        try:
            transform_set_point = self.tf_buffer.transform(data, self.world_frame, rospy.Duration(1))
            set_point = np.array([transform_set_point.pose.position.x,
                                  transform_set_point.pose.position.y,
                                  transform_set_point.pose.position.z])

            current_quaternion = (transform_set_point.pose.orientation.x,
                                  transform_set_point.pose.orientation.y,
                                  transform_set_point.pose.orientation.z,
                                  transform_set_point.pose.orientation.w)
            # current_yaw, _, _ = transformations.euler_from_quaternion(current_quaternion, axes='szyx')
            _, _, current_yaw = transformations.euler_from_quaternion(current_quaternion)

            set_point_yaw = np.unwrap(np.array([self.set_point_yaw[0], current_yaw]))[-1]

            # Check if set-point is in the allowed space
            if self._check_point_in_room(set_point[0], set_point[1], set_point[2]):
                # Update set point
                self.set_point = set_point
                self.set_point_yaw[0] = set_point_yaw
                result = True
        except tf2.LookupException:
            print("ERROR: No transformation between {} and {}.".format(self.drone_frame, self.world_frame))
        return result

    def reset_pitch_roll_yaw(self):
        result = False
        try:
            transform_current_pose = self.tf_buffer.lookup_transform(self.world_frame, self.drone_frame, rospy.Time(0))

            current_pose = np.array([transform_current_pose.transform.translation.x,
                                     transform_current_pose.transform.translation.y,
                                     transform_current_pose.transform.translation.z])
            current_quaternion = (transform_current_pose.transform.rotation.x,
                                  transform_current_pose.transform.rotation.y,
                                  transform_current_pose.transform.rotation.z,
                                  transform_current_pose.transform.rotation.w)
            # current_yaw, _, _ = transformations.euler_from_quaternion(current_quaternion, axes='szyx')
            _, _, current_yaw = transformations.euler_from_quaternion(current_quaternion)

            # Update set point and reset the time
            self.ma_filter.reset_component(0, current_pose[0])
            self.ma_filter.reset_component(1, current_pose[1])
            self.ma_filter.reset_component(3, current_yaw)

            self.low_pass_filter.reset_component(0, current_pose[0])
            self.low_pass_filter.reset_component(1, current_pose[1])
            self.low_pass_filter.reset_component(3, current_yaw)

            self.set_point[0] = current_pose[0]
            self.set_point[1] = current_pose[1]
            self.set_point_yaw[0] = current_yaw
            result = True
        except tf2.LookupException:
            print("ERROR: No transformation between {} and {}.".format(self.drone_frame, self.world_frame))
        return result

    def publish_guided_setpoint(self, x, y, z, yaw):
        setpoint = PoseStamped()
        setpoint.header.stamp = rospy.Time.now()
        setpoint.header.frame_id = 'map'
        setpoint.pose.position.x = x
        setpoint.pose.position.y = y
        setpoint.pose.position.z = z
        quaternion_desired = transformations.quaternion_from_euler(0, 0, yaw)
        setpoint.pose.orientation.x = quaternion_desired[0]
        setpoint.pose.orientation.y = quaternion_desired[1]
        setpoint.pose.orientation.z = quaternion_desired[2]
        setpoint.pose.orientation.w = quaternion_desired[3]
        self.guid_set_point_publisher.publish(setpoint)

    # publish attitude msh for angle mode
    def publish_attitude_angle(self, pitch, roll, yaw, trust):
        msg = AttitudeTarget()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = self.drone_frame
        msg.type_mask = msg.IGNORE_PITCH_RATE | msg.IGNORE_ROLL_RATE | msg.IGNORE_YAW_RATE
        # quat = transformations.quaternion_from_euler(yaw, roll, pitch, axes='szyx')
        quat = transformations.quaternion_from_euler(roll, pitch, yaw)
        msg.orientation.x = quat[0]
        msg.orientation.y = quat[1]
        msg.orientation.z = quat[2]
        msg.orientation.w = quat[3]
        msg.thrust = trust
        self.fcu_set_point_publisher.publish(msg)

    # publish attitude msh for acrobatic mode
    def publish_attitude_acro(self, wx, wy, wz, trust):
        msg = AttitudeTarget()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = self.drone_frame
        msg.type_mask = msg.IGNORE_ATTITUDE
        msg.body_rate.x = wx
        msg.body_rate.y = wy
        msg.body_rate.z = wz
        msg.thrust = trust
        self.fcu_set_point_publisher.publish(msg)

    def publish_diagnostics(self, log):
        msg = DiagnosticArray()
        msg.header.stamp = rospy.Time.now()
        msg.status = []
        status = DiagnosticStatus()
        status.level = 0
        status.name = "DroneController"
        status.message = "Log"
        status.hardware_id = "PixRacer R15"
        status.values = []
        for key in log:
            key_value = KeyValue()
            key_value.key = key
            key_value.value = str(log[key])
            status.values.append(key_value)

        msg.status.append(status)

        self.diagnostic_publisher.publish(msg)

    def go_home(self, data):
        result = False
        if self.current_state == self.drone_states["FLYING"]:
            point = PoseStamped()
            point.header.frame_id = self.world_frame
            point.pose.position.x = self.home[0]
            point.pose.position.y = self.home[1]
            point.pose.position.z = self.home[2] + self.takeoff_altitude

            # q = transformations.quaternion_from_euler(self.home_yaw[0], 0, 0, axes='szyx')
            q = transformations.quaternion_from_euler(0, 0, self.home_yaw[0])

            point.pose.orientation.x = q[0]
            point.pose.orientation.y = q[1]
            point.pose.orientation.z = q[2]
            point.pose.orientation.w = q[3]

            result = self.update_set_point(point)

        return result

    def _publish_point(self, point, ID, yaw=0.0, r=0.0, g=1.0, b=0.0):
        marker = Marker()
        marker.header.stamp = rospy.Time.now()
        marker.header.frame_id = self.world_frame
        marker.ns = "set_point"
        marker.id = ID
        marker.type = 0
        marker.action = 0
        marker.pose.position.x = point[0]
        marker.pose.position.y = point[1]
        marker.pose.position.z = point[2]
        # q = transformations.quaternion_from_euler(yaw, 0, 0, axes='szyx')
        q = transformations.quaternion_from_euler(0, 0, yaw)
        marker.pose.orientation.x = q[0]  # Fix Quaternion Warning
        marker.pose.orientation.y = q[1]  # Fix Quaternion Warning
        marker.pose.orientation.z = q[2]  # Fix Quaternion Warning
        marker.pose.orientation.w = q[3]  # Fix Quaternion Warning
        marker.scale.x = 0.05
        marker.scale.y = 0.05
        marker.scale.z = 0.05
        marker.color.r = r
        marker.color.g = g
        marker.color.b = b
        marker.color.a = 1.0

        self.visualization_publisher.publish(marker)

    def _publish_safety_room(self):
        # Room Marker
        ID = 0
        x = (self.room_max_x - self.room_min_x) / 2 + self.room_min_x
        y = (self.room_max_y - self.room_min_y) / 2 + self.room_min_y
        z = (self.room_max_z - self.room_min_z) / 2 + self.room_min_z
        scale_x = self.room_max_x - self.room_min_x
        scale_y = self.room_max_y - self.room_min_y
        scale_z = self.room_max_z - self.room_min_z

        room = self._make_cube(ID, x, y, z, scale_x, scale_y, scale_z)

        self.visualization_publisher.publish(room)

    def _make_cube(self, ID, x, y, z, scale_x, scale_y, scale_z, r=0.0, g=1.0, b=0.0, a=0.2):
        marker = Marker()
        marker.header.stamp = rospy.Time.now()
        marker.header.frame_id = self.world_frame
        marker.ns = "free_space"
        marker.id = ID
        marker.type = 1
        marker.action = 0
        marker.pose.position.x = x
        marker.pose.position.y = y
        marker.pose.position.z = z
        marker.pose.orientation.w = 1.0  # Fix Quaternion Warning
        marker.scale.x = scale_x
        marker.scale.y = scale_y
        marker.scale.z = scale_z
        marker.color.r = r
        marker.color.g = g
        marker.color.b = b
        marker.color.a = a
        marker.frame_locked = True

        return marker


if __name__ == "__main__":
    controller = Controller()
    while not rospy.is_shutdown():
        # Control Loop
        controller.fsm_loop()
        controller.diagnostic_loop()
        controller.sleep()
