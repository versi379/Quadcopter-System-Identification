import numpy as np
from utils import KalmanFilter, lambda_dyn
import rospy


def yaw_control(R, yh, kth):
    # YAW STEERING
    w3 = kth * np.sin(yh)
    return w3


class DroneLQR:
    def __init__(self, optimal_distance=0.0):

        self._optimal_distance = optimal_distance

        # Get Parameters
        global_parameter_name = "/drone_controller"

        # TrustAsTrust Hovering value
        self.TRUST_STATIC = rospy.get_param("{}/static_trust".format(global_parameter_name))  # Drone ThrustAsThrust
        self.ts = 1 / rospy.get_param("{}/fs".format(global_parameter_name))
        self.g = 9.8
        self.lk = np.log(self.g)

        # REF
        self.rp = np.array([[self._optimal_distance],
                            [0],
                            [0]])
        self.rv = np.array([[0],
                            [0],
                            [0]])
        self.ra = np.array([[0],
                            [0],
                            [0]])

        # CONTROL DESIGN MODEL PARAMETERS
        self.kth = 5

        if self.ts == 0.02:
            self.K = np.array([[4.2, 0, 0, 7.0, 0, 0, 5.6, 0, 0],
                               [0, 4.2, 0, 0, 7.0, 0, 0, 5.6, 0],
                               [0, 0, 4.2, 0, 0, 7.0, 0, 0, 5.6]])

            self.L = np.array([[0.2425, 0, 0],
                                [0, 0.2425, 0],
                                [0, 0, 0.2425],
                                [1.3857, 0, 0],
                                [0, 1.3857, 0],
                                [0, 0, 1.3857],
                                [3.9610, 0, 0],
                                [0, 3.9610, 0],
                                [0, 0, 3.9610]])

            self.C = np.concatenate([np.eye(3), np.zeros((3, 3)), np.zeros((3, 3))], axis=1)

            self.Akf = np.array([[1.0, 0, 0, 0.02, 0, 0, 0.0002, 0, 0],
                                [0, 1.0, 0, 0, 0.02, 0, 0, 0.0002, 0],
                                [0, 0, 1.0, 0, 0, 0.02, 0, 0, 0.0002],
                                [0, 0, 0, 1.0, 0, 0, 0.02, 0, 0],
                                [0, 0, 0, 0, 1.0, 0, 0, 0.02, 0],
                                [0, 0, 0, 0, 0, 1.0, 0, 0, 0.02],
                                [0, 0, 0, 0, 0, 0, 1.0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1.0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 1.0]])

            self.Bkf = np.array([[0.0, 0, 0],
                                 [0, 0.0, 0],
                                 [0, 0, 0.0],
                                 [0.0002, 0, 0],
                                 [0, 0.0002, 0],
                                 [0, 0, 0.0002],
                                 [0.0200, 0, 0],
                                 [0, 0.0200, 0],
                                 [0, 0, 0.0200]])

        elif self.ts == 0.05:
            self.K = np.array([[15.4687, 0, 0, 35.7607, 0, 0, 25.8673, 0, 0],
                               [0, 15.4687, 0, 0, 35.7607, 0, 0, 25.8673, 0],
                               [0, 0, 15.4687, 0, 0, 35.7607, 0, 0, 25.8673]])

            self.L = np.array([[0.6743, 0, 0],
                                [0, 0.6743, 0],
                                [0, 0, 0.6743],
                                [3.8916, 0, 0],
                                [0, 3.8916, 0],
                                [0, 0, 3.8916],
                                [11.2499, 0, 0],
                                [0, 11.2499, 0],
                                [0, 0, 11.2499]])

            self.C = np.concatenate([np.eye(3), np.zeros((3, 3)), np.zeros((3, 3))], axis=1)

            self.Akf = np.array([[1.0, 0, 0, 0.0500, 0, 0, 0.0013, 0, 0],
                                [0, 1.0, 0, 0, 0.0500, 0, 0, 0.0013, 0],
                                [0, 0, 1.0, 0, 0, 0.0500, 0, 0, 0.0013],
                                [0, 0, 0, 1.0, 0, 0, 0.0500, 0, 0],
                                [0, 0, 0, 0, 1.0, 0, 0, 0.0500, 0],
                                [0, 0, 0, 0, 0, 1.0, 0, 0, 0.0500],
                                [0, 0, 0, 0, 0, 0, 1.0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1.0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 1.0]])

            self.Bkf = np.array([[0.0, 0, 0],
                                 [0, 0.0, 0],
                                 [0, 0, 0.0],
                                 [0.0013, 0, 0],
                                 [0, 0.0013, 0],
                                 [0, 0, 0.0013],
                                 [0.0500, 0, 0],
                                 [0, 0.0500, 0],
                                 [0, 0, 0.0500]])

        else:
            print("The LQR Agents only supports the following ts: 0.05 (20Hz) - 0.01 (100Hz)")
            exit(-1)

        self.kalman_filter = KalmanFilter(Akf=self.Akf, Bkf=self.Bkf, L=self.L, C=self.C)
        self.kalman_init = False

    def perform_action(self, observation, take_off=False) -> tuple:
        p0 = observation["p"]
        R = observation["R"]
        yaw = observation["yaw"]
        if not self.kalman_init:
            self.kalman_filter.reset(p0=p0)
            self.kalman_init = True

        x_est = self.kalman_filter.state

        # Control commands computation
        # position control
        error = self.rp - x_est[:][:3]
        d_error = self.rv - x_est[:][3:6]
        dd_error = self.ra - x_est[:][6:]
        u = - np.dot(self.K, np.concatenate([error, d_error, dd_error]).reshape((9, 1)))

        # Yaw control
        omega3 = yaw_control(R, yaw, self.kth)

        # Output
        f = np.exp(self.lk) * self.TRUST_STATIC / 9.8
        q = np.dot(R.T, u) / np.exp(self.lk)
        wtr = np.zeros((3, 1))
        wtr[0] = -q[1]
        wtr[1] = q[0]
        wtr[2] = omega3
        # wtr[2] = 0.0
        dlam = q[2]

        self.lk = lambda_dyn(dlam, self.lk, self.ts)

        if take_off:
            self.kalman_filter.filter(p0, np.zeros_like(u))
        else:
            self.kalman_filter.filter(p0, u)

        return wtr, f

    def reset(self) -> None:
        self.lk = np.log(self.g)
        self.kalman_init = False

    def filter(self, p, u) -> None:
        if not self.kalman_init:
            self.kalman_filter.reset(p0=p)
            self.kalman_init = True
        self.kalman_filter.filter(p, u)
