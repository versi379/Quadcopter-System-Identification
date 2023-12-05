#! /usr/bin/python3
import rospy
import time
import copy
import tf2_ros as tf2
import numpy as np
from threading import Thread
from tf import transformations
from mavros_msgs.msg import AttitudeTarget, State
from mavros_msgs.srv import CommandBool, SetMode, SetModeRequest

class TestDrone:

    def __init__(self):

        rospy.init_node("drone_flight")

        self.world_frame = "map"
        self.drone_frame = "base_link"

        self.rate_control_loop = rospy.Rate(100)
        self.rate_pose_loop = rospy.Rate(100)

        rospy.wait_for_service("/mavros/cmd/arming")
        self.arming_service = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
        rospy.wait_for_service("/mavros/set_mode")
        self.mode_service = rospy.ServiceProxy('/mavros/set_mode', SetMode)

        self.fcu_set_point_publisher = rospy.Publisher('/mavros/setpoint_raw/attitude', AttitudeTarget, queue_size=1)

        self.tf_buffer = tf2.Buffer()
        self.tf_listener = tf2.TransformListener(self.tf_buffer)
        
        try:
            transform = self.tf_buffer.lookup_transform(self.world_frame, self.drone_frame, rospy.Time(0),
                                                        rospy.Duration(5))
        except tf2.LookupException:
            print("ERROR: No transformation between {} and {}. Cannot initialize the node. Exiting...".format(
                self.world_frame, self.drone_frame))
            exit(-1)

        self.init_pose = np.array([transform.transform.translation.x,
                                   transform.transform.translation.y,
                                   transform.transform.translation.z])
        
        self.current_pose = copy.deepcopy(self.init_pose)
        
        self.init_orientation = np.array([transform.transform.rotation.x,
                               transform.transform.rotation.y,
                               transform.transform.rotation.z,
                               transform.transform.rotation.w])

        self.current_orientation = copy.deepcopy(self.init_orientation)

        self.thread_control_loop = Thread(target=self._control_loop)
        self.thread_pose_loop = Thread(target=self._pose_loop)
        self.thread_control_loop.start()
        self.thread_pose_loop.start()

        self.output_data = np.array([[self.init_pose[0], self.init_pose[1], self.init_pose[2]]])


    def _control_loop(self):
        while True:
            self.take_off()

            fly = True
            while fly:
                self.publish_attitude_angle(0, 0, 0, 0.55)
                if self.current_pose[2] > 0 and time.time() <= time.time() + 10:
                    np.append(self.output_data, [[self.current_pose[0], self.current_pose[1], self.current_pose[2]]], axis=0)
                    print("[{}] {} {} {}".format(time.time(), self.current_pose[0], self.current_pose[1], self.current_pose[2]))
                else:
                    fly = False

            np.savetxt('output_data.csv', self.output_data, delimiter="   ")
            
            self.rate_control_loop.sleep()

    def _pose_loop(self):
        while True:
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

            self.rate_pose_loop.sleep()

    def take_off(self):
        current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(2))
        if current_state.mode != "GUIDED":
            offb_set_mode = SetModeRequest()
            offb_set_mode.custom_mode = "GUIDED"
            self.mode_service.call(offb_set_mode)
            time.sleep(1.0)
            current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(2))
            if current_state.mode != "GUIDED":
                rospy.loginfo("Cannot set mode GUIDED")
                return False
        start_timer = time.time()
        armed = False
        while not (armed and start_timer + 15.0 > time.time()):
            try:
                self.arming_service.call(value=True)
                current_state = rospy.wait_for_message("/mavros/state", State, rospy.Duration(2))
                armed = current_state.armed
            except AttributeError:
                print("AttributeError: maybe the connection has been lost?")
        if not armed:
            rospy.loginfo("Drone not ARMED")
            return False

    def publish_attitude_angle(self, pitch, roll, yaw, trust):
        msg = AttitudeTarget()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = self.drone_frame
        msg.type_mask = msg.IGNORE_PITCH_RATE | msg.IGNORE_ROLL_RATE | msg.IGNORE_YAW_RATE
        quat = transformations.quaternion_from_euler(roll, pitch, yaw)
        msg.orientation.x = quat[0]
        msg.orientation.y = quat[1]
        msg.orientation.z = quat[2]
        msg.orientation.w = quat[3]
        msg.thrust = trust
        self.fcu_set_point_publisher.publish(msg)

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

if __name__ == "__main__":
    test = TestDrone()
    while not rospy.is_shutdown():
        pass