import numpy as np


class SingleIntegrator2d:
    def __init__(self, x0: np.array) -> None:
        """
        2D Single integrator class (dt = 1 ignored).
        x_next = A*x_t + B*u_t + w_t
               = x_t + u_t + w_t
        x_next: 2D position at next time step
        A: dynamics matrix
        x_t: 2D position at current time step
        B: input matrix
        u_t: control input
        w_t: noise
        :param x0: initial position of the robot
        """
        self.A = np.diag([1, 1])
        self.B = np.diag([1, 1])

        self.x_t = x0  # current state initialized to initial position
        self.u_t = np.zeros([2, ])  # current control initialized to zero
        self.x_next = x0  # next state initialized to current position
        self.w_t = np.zeros([2, ])  # noise = 0 --> we know exactly where we are

    def step(self, u_t: np.ndarray, w_t: np.ndarray = np.zeros([2, ])) -> np.ndarray:
        """
        Computes the true next state x_next = A*x_t + B*u_t + w_t
        :param u_t: control input
        :param w_t: noise realization
        :return: realized/observed/true next state
        """
        self.u_t = u_t  # update current control
        self.w_t = w_t  # update the realized noise (affects next state)
        self.x_next = self.A @ self.x_t + self.B @ self.u_t + self.w_t  # compute and update the next state
        self.x_t = self.x_next  # update the current position to the next position
        return self.x_t  # return the next state

    def predict(self, x_t: np.ndarray, u_t: np.ndarray, w_mean_t: np.ndarray) -> np.ndarray:
        """
        Computes the expected state x_next = A*x_t + B*u_t + w_mean_t
        :param x_t: current state
        :param u_t: current control
        :param w_mean_t: average noise value
        :return: expected next state
        """
        # return a prediction of the next state using nominal values
        return self.A @ x_t + self.B @ u_t + w_mean_t
