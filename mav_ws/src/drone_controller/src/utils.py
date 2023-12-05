import numpy as np
import collections
from statistics import mean
import time
import warnings


class LowPassFilter:
    def __init__(self, init_state, Tc, ts):
        self._state = init_state
        self.Tc = Tc
        self.ts = ts

    def reset(self, init_state=None, ts=None):
        if init_state is not None:
            self._state = init_state
        if ts is not None:
            self.ts = ts

    def reset_component(self, component, value):
        try:
            self._state[component] = value
        except IndexError:
            print("ERROR: could not reset specified component. IndexError")

    def filter(self, ref):
        A = np.eye(ref.shape[0]) * np.exp(-(self.ts / self.Tc))
        B = np.eye(ref.shape[0]) * (1 - np.exp(-(self.ts / self.Tc)))
        self._state = np.dot(A, self._state) + np.dot(B, ref)
        return self._state

    @property
    def state(self):
        return self._state


class MAFilter:
    def __init__(self, init_state, Tc, ts):
        self._state = init_state
        self.Tc = Tc
        self.ts = ts
        self.buffers = []
        for i in range(len(self._state)):
            buffer = collections.deque([self._state[i]] * int(self.Tc / self.ts))
            self.buffers.append(buffer)

        print(len(self.buffers), len(self.buffers[0]))

    def reset(self, init_state=None, ts=None):
        if init_state is not None:
            self._state = init_state
        if ts is not None:
            self.ts = ts

    def reset_component(self, component, value):
        try:
            self.buffers[component] = collections.deque([value] * int(self.Tc / self.ts))
        except IndexError:
            print("ERROR: could not reset specified component. IndexError")

    def filter(self, ref):
        for i in range(len(ref)):
            self.buffers[i].append(ref[i])
            self.buffers[i].popleft()

        return np.array([mean(buffer) for buffer in self.buffers])

    @property
    def state(self):
        return np.array([mean(buffer) for buffer in self.buffers])


class VelocityFIR:
    def __init__(self, l=4, T=0.05):
        self.l = l
        assert 1 < l < 9

        if l == 2:
            self.coeff = np.array([1, -1]).reshape((1, l))
        elif l == 3:
            self.coeff = np.array([.5, 0, -.5]).reshape((1, l))
        elif l == 4:
            self.coeff = np.array([.3, .1, -.1, -.3]).reshape((1, l))
        elif l == 5:
            self.coeff = np.array([.2, .1, 0, -.1, -.2]).reshape((1, l))
        elif l == 6:
            self.coeff = np.array([1/7, 3/35, 1/35, -1/35, -3/35, -1/7]).reshape((1, l))
        elif l == 7:
            self.coeff = np.array([3/28, 1/14, 1/28, 0, -1/28, -1/14, -3/28]).reshape((1, l))
        elif l == 8:
            self.coeff = np.array([1/12, 5/84, 1/28, 1/84, -1/84, -1/28, -5/84, -1/12]).reshape((1, l))

        self.coeff = self.coeff / T

        self.state = None
        self.init = False

    def filter(self, p):
        p = p.reshape((-1, 1))
        if not self.init:
            self.state = [p] * self.l
            self.init = True
        self.state.insert(0, p)
        self.state.pop(-1)

        buffer = np.concatenate(self.state, axis=1)
        r, _ = buffer.shape
        weights = np.concatenate([self.coeff] * r, axis=0)

        velocities = np.sum(np.multiply(buffer, weights), axis=1)

        return velocities

    def reset(self, p):
        p = p.reshape((-1, 1))
        self.state = [p] * self.l
        self.init = True


def lambda_dyn(dlam, lk, Ts):
    lk1 = lk + dlam * Ts
    return lk1


class KalmanFilter:
    def __init__(self, Akf, Bkf, L, C, p0=np.zeros((3, 1)), v0=np.zeros((3, 1)), a0=np.zeros((3, 1))):
        self.filter_state = np.concatenate([p0, v0, a0]).reshape(9, 1)

        self.Akf = Akf
        self.Bkf = Bkf
        self.L = L
        self.C = C

    @property
    def state(self):
        return self.filter_state

    def filter(self, p, u):
        # Kalman filter dynamics
        self.filter_state = np.dot(self.Akf, self.filter_state) - np.dot(self.Bkf, u) + np.dot(self.L, np.array(p).reshape(3, 1) - np.dot(self.C, self.filter_state))

    def reset(self, p0=np.zeros((3, 1)), v0=np.zeros((3, 1)), a0=np.zeros((3, 1))):
        p0 = p0.reshape((3, 1))
        v0 = v0.reshape((3, 1))
        a0 = a0.reshape((3, 1))
        self.filter_state = np.concatenate([p0, v0, a0]).reshape(9, 1)


def _clamp(value, limits):
    lower, upper = limits
    if value is None:
        return None
    elif (upper is not None) and (value > upper):
        return upper
    elif (lower is not None) and (value < lower):
        return lower
    return value


try:
    # Get monotonic time to ensure that time deltas are always positive
    _current_time = time.monotonic
except AttributeError:
    # time.monotonic() not available (using python < 3.3), fallback to time.time()
    _current_time = time.time
    warnings.warn('time.monotonic() not available in python < 3.3, using time.time() as fallback')


class PID(object):
    """A simple PID controller."""

    def __init__(
        self,
        Kp=1.0,
        Ki=0.0,
        Kd=0.0,
        int_init=0.0,
        sample_time=0.01,
        velocity_fir_window=4,
        output_limits=(-np.inf, np.inf),
        windup_limits=(-np.inf, np.inf)
    ):
        """
        Initialize a new PID controller.

        :param Kp: The value for the proportional gain Kp
        :param Ki: The value for the integral gain Ki
        :param Kd: The value for the derivative gain Kd
        :param int_init: The initial integral value
        :param sample_time: The time in seconds which the controller should wait before generating
            a new output value. The PID works best when it is constantly called (eg. during a
            loop), but with a sample time set so that the time difference between each update is
            (close to) constant. If set to None, the PID will compute a new output value every time
            it is called.
        :param output_limits: The initial output limits to use, given as an iterable with 2
            elements, for example: (lower, upper). The output will never go below the lower limit
            or above the upper limit. Either of the limits can also be set to None to have no limit
            in that direction. Setting output limits also avoids integral windup, since the
            integral term will never be allowed to grow outside of the limits.
        :param proportional_on_measurement: Whether the proportional term should be calculated on
            the input directly rather than on the error (which is the traditional way). Using
            proportional-on-measurement avoids overshoot for some types of systems.
        """
        assert isinstance(output_limits, tuple) and list(map(type, output_limits)) == [float, float]
        assert isinstance(windup_limits, tuple) and list(map(type, output_limits)) == [float, float]

        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.sample_time = sample_time
        self.int_init = int_init
        self.velocity_fir_window = velocity_fir_window
        self.velocity_fir = VelocityFIR(velocity_fir_window, self.sample_time)

        self.output_limits = output_limits
        self.windup_limits = windup_limits

        self._min_output_windup, self._max_output_windup = self.windup_limits
        self._min_output, self._max_output = self.output_limits
        if self.Ki != 0:
            self._error_integral = self.int_init / self.Ki
        else:
            self._error_integral = 0.0

        self._proportional = 0
        self._integral = self.int_init
        self._derivative = 0

        self.last_time = None

        try:
            # Get monotonic time to ensure that time deltas are always positive
            self.time_fn = time.monotonic
        except AttributeError:
            # time.monotonic() not available (using python < 3.3), fallback to time.time()
            self.time_fn = time.time

    def __call__(self, input_, mes=None):
        """
        Update the PID controller.

        Call the PID controller with *input_* and calculate and return a control output at
        sample_time seconds.

        """
        if self.last_time is None:
            self.last_time = self.time_fn()
        current_time = self.time_fn()
        dt = current_time - self.last_time
        self.last_time = current_time
        # Compute error terms
        error = input_
        if mes is not None:
            d_error = self.velocity_fir.filter(-mes)[0]
        else:
            d_error = self.velocity_fir.filter(input_)[0]

        self._proportional = self.Kp * error
        self._integral = self.Ki * self._error_integral
        self._derivative = self.Kd * d_error

        if self.Ki != 0:
            self._error_integral = np.clip(self._error_integral + error * self.sample_time,
                                           self._min_output_windup / self.Ki,
                                           self._max_output_windup / self.Ki)

        # Compute final output
        output = self._proportional + self._integral + self._derivative
        output = np.clip(output, self._min_output, self._max_output)

        return output

    def __repr__(self):
        return (
            '{self.__class__.__name__}('
            'Kp={self.Kp!r}, Ki={self.Ki!r}, Kd={self.Kd!r}, '
            'int_init={self.int_init!r}, sample_time={self.sample_time!r}, '
            'velocity_fir_window={self.velocity_fir_window!r}, '
            'output_limits={self.output_limits!r}, windup_limits={self.windup_limits!r},'
            ')'
        ).format(self=self)

    @property
    def components(self):
        """
        The P-, I- and D-terms from the last computation as separate components as a tuple. Useful
        for visualizing what the controller is doing or when tuning hard-to-tune systems.
        """
        return self._proportional, self._integral, self._derivative

    @property
    def tunings(self):
        """The tunings used by the controller as a tuple: (Kp, Ki, Kd)."""
        return self.Kp, self.Ki, self.Kd

    def reset(self):
        """
        Reset the PID controller internals.

        This sets each term to 0 as well as clearing the integral, the last output and the last
        input (derivative calculation).
        """
        if self.Ki != 0:
            self._error_integral = self.int_init / self.Ki
        else:
            self._error_integral = 0.0

        self._proportional = 0
        self._integral = self.int_init
        self._derivative = 0
        self.last_time = None
