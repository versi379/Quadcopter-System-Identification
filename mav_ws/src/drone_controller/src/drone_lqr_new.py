import numpy as np
from utils import lambda_dyn
import rospy


def lambda_dyn(dlam, lk, Ts):
    lk1 = lk + dlam * Ts
    return lk1


def yaw_control(R, yh, kth):
    # yh = np.arctan2(np.dot(R[:,1:2].T, yp), np.dot(R[:,0:1].T, yp))
    return kth * np.sin(yh)


class NewDroneLQR:
    def __init__(self, optimal_distance=0.0):

        self._optimal_distance = optimal_distance

        # Get Parameters
        global_parameter_name = "/drone_controller"

        # TrustAsTrust Hovering value
        self.TRUST_STATIC = rospy.get_param("{}/static_trust".format(global_parameter_name))  # Drone ThrustAsThrust
        self.ts = 1 / rospy.get_param("{}/fs".format(global_parameter_name))

        # drone parameters
        self.g = 9.8
        # self.m = 1  # actual drone mass [kg]
        # self.mnom = 1  # lqr design mass [kg]

        # control parameters
        self.kth = 5
        # self.lk = np.log(self.m / self.mnom * self.g)
        self.lk = self.g
        # self.lk = self.TRUST_STATIC
        self.rp = np.vstack(np.array([self._optimal_distance, 0, 0]))

        if self.ts == 0.01:
            self.KdA = np.array([
                [0.515950326540711, -0.423531209942170, -0.380875411664983, -0.069429417520758, 0.051941174156612,
                 0.002467288979541, -0.000158460050222, 0.000013927037154, -0.000022469578793, -0.000074853982520,
                 -0.000040099454413, -0.000003399398242],
                [0.423531209942170, 0.858239107288315, -0.216320605307937, -0.001517860212765, -0.015290817690412,
                 0.001970717736746, 0.000226129794259, 0.000028392886246, -0.000026152756138, -0.000331313590800,
                 0.000016446749054, 0.000002277668745],
                [0.380875411664983, -0.216320605307937, 0.169767332197724, 0.238610640937246, -0.207785525697116,
                 0.025255494586709, -0.001727542223706, 0.000429167199846, -0.000106151596231, -0.002441634691017,
                 -0.000089079521802, -0.000003081846628],
                [-0.069429417520758, 0.001517860212765, -0.238610640937246, 0.889854804578762, 0.214474340805591,
                 -0.003465484101764, -0.004775656631927, 0.000017967571527, 0.000253044402205, 0.002211914767288,
                 -0.000313486399256, -0.000034382617997],
                [0.051941174156611, 0.015290817690412, 0.207785525697116, 0.214474340805591, 0.113675505293258,
                 -0.047814447083151, 0.063767973858981, -0.001938186709034, -0.002870421440603, -0.017090833949584,
                 0.003781838077154, 0.000396628527177],
                [-0.002467288979541, 0.001970717736748, 0.025255494586714, 0.003465484101760, 0.047814447083214,
                 0.004975232243456, -0.351041135851599, -0.008649155913296, 0.037266375458249, 0.160709963010356,
                 0.005227174825194, -0.000104887949700],
                [-0.000158460050226, -0.000226129794259, 0.001727542223682, -0.004775656631935, 0.063767973858955,
                 0.351041135852167, 0.679138458062615, -0.081525642774705, 0.034850845694964, 0.335396278558900,
                 -0.005667668446788, -0.001347097986630],
                [-0.000013927037153, 0.0000283928862468, 0.000429167199850, -0.000017967571526, 0.001938186709037,
                 -0.008649155913220, 0.081525642774671, 0.994700267095457, 0.008218480047146, 0.035786298070896,
                 -0.002434671972228, -0.000318239703294],
                [-0.000022469578793, 0.000026152756138, 0.000106151596230, 0.000253044402205, -0.002870421440603,
                 -0.037266375458232, 0.034850845694970, -0.008218480047136, 0.994055835540180, -0.077064215444723,
                 -0.004002366297469, -0.000255655298800],
                [0.000074853982519, -0.000331313590799, -0.002441634691012, -0.002211914767285, 0.017090833949587,
                 0.160709963009978, -0.335396278559077, 0.035786298070862, 0.077064215444681, 0.476128072322979,
                 0.135483831896387, 0.012511519416148],
                [-0.000040099454419, -0.000016446749057, 0.000089079521772, -0.000313486399261, 0.003781838077141,
                 -0.005227174825021, -0.005667668446473, 0.002434671972244, -0.004002366297526, -0.135483831896379,
                 0.951227759985636, -0.006761017626969],
                [-0.000003399398243, -0.000002277668746, 0.000003081846621, -0.000034382617998, 0.000396628527174,
                 0.000104887949742, -0.001347097986568, 0.000318239703298, -0.000255655298809, -0.012511519416149,
                 -0.006761017626969, 0.998810161967763]
            ])
            self.KdB = np.array([
                [2.1036416413645],
                [0.1970014173364],
                [-0.9940619919771],
                [0.0383115644965],
                [0.0580758059595],
                [0.0191061686879],
                [0.0000731805472],
                [0.0002260437896],
                [0.0001668211258],
                [-0.0018141192142],
                [0.0000751141706],
                [0.0000025588640],
            ])
            self.kdC = np.array(
                [183.103287282781, 44.1662136856455, 211.023353221758, -42.2306511301680, 111.775262262962,
                 23.2176334774270, 1.26484386797251, 0.714429858253983, -0.166902981764340, -5.95939943888813,
                 0.498175097435377, 0.0578999940445104])
            self.kdD = 0
            self.xest1 = np.zeros((len(self.KdA), 1))
            self.xest2 = np.zeros((len(self.KdA), 1))
            self.xest3 = np.zeros((len(self.KdA), 1))
            '''
            self.Af = np.array([
                [0.9703, -0.0148, -0.0099],
                [0.0197, 0.9999, -0.0001],
                [0.0000, 0.0050, 1.0000]
            ])
            self.Bf = np.array([
                [0.0099],
                [0.0001],
                [0.0000]
            ])
            self.Cf = np.array([0, 0, 1])
            self.Df = 0
            self.xf1 = np.array([
                [0],
                [0],
                [0]
                # [xr[0,0] - p[0,0]]
            ])
            self.xf2 = np.array([
                [0],
                [0],
                [0]
                # [xr[1,0] - p[1,0]]
            ])
            self.xf3 = np.array([
                [0],
                [0],
                [0]
                # [xr[2,0] - p[2,0]]
            ])
            '''
        else:
            print("The LQR Agents only supports the following ts: 0.01 (100Hz)")
            exit(-1)

    def perform_action(self, observation, take_off=False) -> tuple:
        yp = observation["p"]
        R = observation["R"]
        yaw = observation["yaw"]
        '''
        rf1 = np.dot(self.Cf, self.xf1) + np.dot(self.Df, self.rp[0][0])
        self.xf1 = np.dot(self.Af, self.xf1) + np.dot(self.Bf, self.rp[0][0])
        rf2 = np.dot(self.Cf, self.xf2) + np.dot(self.Df, self.rp[1][0])
        self.xf2 = np.dot(self.Af, self.xf2) + np.dot(self.Bf, self.rp[1][0])
        rf3 = np.dot(self.Cf, self.xf3) + np.dot(self.Df, self.rp[2][0])
        self.xf3 = np.dot(self.Af, self.xf3) + np.dot(self.Bf, self.rp[2][0])
        rf = np.vstack([rf1[0], rf2[0], rf3[0]])
        inpcop = rf - yp
        '''
        inpcop = yp.T
        u1 = np.dot(self.kdC, self.xest1) + np.dot(self.kdD, inpcop[0][0])
        self.xest1 = np.dot(self.KdA, self.xest1) + np.dot(self.KdB, inpcop[0][0])
        u2 = np.dot(self.kdC, self.xest2) + np.dot(self.kdD, inpcop[1][0])
        self.xest2 = np.dot(self.KdA, self.xest2) + np.dot(self.KdB, inpcop[1][0])
        u3 = np.dot(self.kdC, self.xest3) + np.dot(self.kdD, inpcop[2][0])
        self.xest3 = np.dot(self.KdA, self.xest3) + np.dot(self.KdB, inpcop[2][0])
        u = np.vstack([u1, u2, u3])
        # omega3 = yaw_control(R, yaw, self.kth)
        omega3 = 0
        # f = np.exp(self.lk) * self.mnom
        '''
        f = np.exp(self.lk) * self.TRUST_STATIC / self.g
        q = np.exp(-self.lk) * np.dot(R.T, u)
        '''
        # f = self.mnom * self.lk
        f = (self.TRUST_STATIC / self.g) * self.lk
        # f = (self.TRUST_STATIC / self.g) * (9.8+0.1)
        q = np.dot(R.T, u)
        wtr = np.zeros((3, 1))
        wtr[0][0] = -q[1][0] / self.lk
        wtr[1][0] = q[0][0] / self.lk
        wtr[2][0] = omega3
        dlam = q[2][0]
        #wtr[0][0] = 0
        #wtr[1][0] = 0
        #wtr[2][0] = 0
        #dlam = 0
        self.lk = lambda_dyn(dlam, self.lk, self.ts)
        # print("inpcop: {:2.10f} {:2.10f} {:2.10f} | f: {:2.10f}".format(inpcop.flatten()[0], inpcop.flatten()[1], inpcop.flatten()[2], f))
        return wtr, f
