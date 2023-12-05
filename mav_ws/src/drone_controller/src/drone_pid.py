from utils import PID
import rospy


class DronePid:
    def __init__(self, trust_as_trust=True):

        # CONSTANTS
        self.PITCH_STATIC = 0.0
        self.ROLL_STATIC = 0.0
        self.TRUST_STATIC_CLIMB = 0.5  # Climb

        # Control Z
        self.trust_as_trust = trust_as_trust

        # Get Parameters
        global_parameter_name = "/drone_controller"

        # TrustAsTrust Hovering value
        self.TRUST_STATIC = rospy.get_param("{}/static_trust".format(global_parameter_name))  # Drone ThrustAsThrust

        ts = 1 / rospy.get_param("{}/fs".format(global_parameter_name))

        # PID Pitch
        Kp_x = rospy.get_param("{}/Kp_x".format(global_parameter_name))
        Ki_x = rospy.get_param("{}/Ki_x".format(global_parameter_name))
        Kd_x = rospy.get_param("{}/Kd_x".format(global_parameter_name))
        init_d_x = rospy.get_param("{}/init_d_x".format(global_parameter_name))
        output_limit_min_x = rospy.get_param("{}/output_limit_min_x".format(global_parameter_name))
        output_limit_max_x = rospy.get_param("{}/output_limit_max_x".format(global_parameter_name))
        windup_limit_min_x = rospy.get_param("{}/windup_limit_min_x".format(global_parameter_name))
        windup_limit_max_x = rospy.get_param("{}/windup_limit_max_x".format(global_parameter_name))

        self.pid_x = PID(Kp=Kp_x,
                         Ki=Ki_x,
                         Kd=Kd_x,
                         int_init=init_d_x,
                         output_limits=(output_limit_min_x, output_limit_max_x),
                         windup_limits=(windup_limit_min_x, windup_limit_max_x),
                         sample_time=ts)

        print("Pitch PID: ", self.pid_x)
        
        # PID Roll
        Kp_y = rospy.get_param("{}/Kp_y".format(global_parameter_name))
        Ki_y = rospy.get_param("{}/Ki_y".format(global_parameter_name))
        Kd_y = rospy.get_param("{}/Kd_y".format(global_parameter_name))
        init_d_y = rospy.get_param("{}/init_d_y".format(global_parameter_name))
        output_limit_min_y = rospy.get_param("{}/output_limit_min_y".format(global_parameter_name))
        output_limit_max_y = rospy.get_param("{}/output_limit_max_y".format(global_parameter_name))
        windup_limit_min_y = rospy.get_param("{}/windup_limit_min_y".format(global_parameter_name))
        windup_limit_max_y = rospy.get_param("{}/windup_limit_max_y".format(global_parameter_name))

        self.pid_y = PID(Kp=Kp_y,
                         Ki=Ki_y,
                         Kd=Kd_y,
                         int_init=init_d_y,
                         output_limits=(output_limit_min_y, output_limit_max_y),
                         windup_limits=(windup_limit_min_y, windup_limit_max_y),
                         sample_time=ts)

        print("Roll PID: ", self.pid_y)

        # PID Altitude
        Kp_z = rospy.get_param("{}/Kp_z".format(global_parameter_name))
        Ki_z = rospy.get_param("{}/Ki_z".format(global_parameter_name))
        Kd_z = rospy.get_param("{}/Kd_z".format(global_parameter_name))
        init_d_z = rospy.get_param("{}/init_d_z".format(global_parameter_name))
        output_limit_min_z = rospy.get_param("{}/output_limit_min_z".format(global_parameter_name))
        output_limit_max_z = rospy.get_param("{}/output_limit_max_z".format(global_parameter_name))
        windup_limit_min_z = rospy.get_param("{}/windup_limit_min_z".format(global_parameter_name))
        windup_limit_max_z = rospy.get_param("{}/windup_limit_max_z".format(global_parameter_name))

        # When ThrustAsThrust is disabled, we do not need an integral contribute
        if not self.trust_as_trust:
            Ki_z = 0.0

        self.pid_z = PID(Kp=Kp_z,
                         Ki=Ki_z,
                         Kd=Kd_z,
                         int_init=init_d_z,
                         output_limits=(output_limit_min_z, output_limit_max_z),
                         windup_limits=(windup_limit_min_z, windup_limit_max_z),
                         sample_time=ts)

        print("Altitude PID: ", self.pid_z)
        print("Altitude Controller SetAttitudeTarget interprets Thrust As Thrust: {} Static Trust: {}".format(self.trust_as_trust, self.TRUST_STATIC))

        # Log
        self.last_output_pitch = 0.0
        self.last_output_roll = 0.0
        self.last_output_trust = 0.0

    def trust(self, error, mes=None):
        trust_output = self.pid_z(error, mes=mes)
        self.last_output_trust = trust_output
        if self.trust_as_trust:
            trust_output_mapped = trust_output * self.TRUST_STATIC / 9.8 + self.TRUST_STATIC  # ThrustAsThrust
        else:
            trust_output_mapped = trust_output * self.TRUST_STATIC_CLIMB / 9.8 + self.TRUST_STATIC_CLIMB  # Climb
        return trust_output_mapped

    def pitch(self, error):
        pitch_output = self.pid_x(error)
        self.last_output_pitch = pitch_output
        pitch_output_mapped = pitch_output / 9.8  # Radians
        return pitch_output_mapped

    def roll(self, error):
        roll_output = -self.pid_y(error)  # Change Sign
        self.last_output_roll = roll_output
        roll_output_mapped = roll_output / 9.8  # Radians
        return roll_output_mapped

    def reset(self):
        self.pid_x.reset()
        self.pid_y.reset()
        self.pid_z.reset()

    @property
    def default_trust(self):
        return self.TRUST_STATIC

    @property
    def default_roll(self):
        return self.ROLL_STATIC

    @property
    def default_pitch(self):
        return self.PITCH_STATIC

    @property
    def pitch_components(self):
        return self.pid_x.components

    @property
    def roll_components(self):
        return self.pid_y.components

    @property
    def trust_components(self):
        return self.pid_z.components

    @property
    def pitch_last_output(self):
        return self.last_output_pitch

    @property
    def roll_last_output(self):
        return self.last_output_roll

    @property
    def trust_last_output(self):
        return self.last_output_trust
