from __future__ import division
import numpy as np

from car_controller.controller import BaseController
from car_controller.controller import compute_position_in_frame


class PIDController(BaseController):
    def __init__(self, **kwargs):
        self.kp = kwargs.pop("kp")
        self.ki = kwargs.pop("ki")
        self.kd = kwargs.pop("kd")

        # For integral control, need an accumulator
        self.error_sum = 0

        # Get the keyword args that we didn't consume with the above initialization
        super(PIDController, self).__init__(**kwargs)

    def reset_params(self, **kwargs):
        with self.state_lock:
            if not set(kwargs).issubset(set(self.__required)):
                raise ValueError(
                    "Invalid or incomplete set of keyword arguments provided", kwargs
                )
            # These next two lines set the instance attributes from the defaults and
            # kwargs dictionaries. For example, the key "kp" becomes the
            # instance attribute self.kp.
            self.__dict__.update(kwargs)

    def reset_state(self):
        super(PIDController, self).reset_state()
        with self.state_lock:
            self.error_sum = 0

    def get_error(self, pose, reference_xytv):
        """Compute the PID error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: across-track and cross-track error
        """
        return compute_position_in_frame(pose, reference_xytv[:3])

    def get_control(self, pose, reference_xytv, error):
        """Compute the PID control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed [x, y, heading, v]
            error: error vector from get_error [e_at, e_ct]

        Returns:
            control: np.array of velocity and steering angle
                (velocity should be copied from reference velocity)
        """
        # BEGIN SOLUTION "QUESTION 2.1" ALT="raise NotImplementedError"
        v_ref = reference_xytv[3]
        e_ct = float(error[1])

        theta = float(pose[2])
        theta_ref = float(reference_xytv[2])
        e_theta = (theta - theta_ref + np.pi) % (2 * np.pi) - np.pi

        d_e_ct = v_ref * np.sin(e_theta)
        dt = 1.0 / self.frequency

        with self.state_lock:
            self.error_sum += e_ct * dt
            alpha = -(self.kp * e_ct + self.ki * self.error_sum + self.kd * d_e_ct)

        return np.array([v_ref, alpha])
        # END SOLUTION