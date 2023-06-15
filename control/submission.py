import numpy as np
from dynamics import SingleIntegrator2d
import matplotlib.pyplot as plt


def proportional_controller(kp: np.ndarray, e_t: np.ndarray) -> np.ndarray:
    """
    compute the proportional control value: u_t = kp * e_t
    :param kp: proportional gain (2x1)
    :param e_t: error signal (2x1)
    :return: control value (2x1)
    """
    # compute the control signal
    u_t = ...  # TODO: add your code
    return u_t


def main():
    t_max = 100  # start/end time
    x0 = np.array([5, 5])  # initial position
    x_goal = np.array([1, 2])  # goal position
    w_mean_t = np.zeros([2, ])  # noise mean
    w_std_dev_t = 0.00 * np.ones([2, ])  # noise standard deviation
    kp = np.array([0.1, 0.1])  # control gains
    dynamics = SingleIntegrator2d(x0=x0)  # dynamics

    # lists to store the simulated and observed states
    x_sim_history = [x0]
    x_history = [x0]

    for t in range(t_max):
        w_t = np.random.normal(w_mean_t, w_std_dev_t)  # noise realization

        x_t = dynamics.x_t  # get current state
        # compute error signal (difference between goal and current value)
        e_t = ...  # TODO: add your code
        # compute control action using the proportional_controller function
        u_t = ...  # TODO: add your code
        # use the dynamics class predict method to predict the next state
        x_next_sim = ...  # TODO: add your code
        # use the dynamics class step method to find the true next state
        x_next = ...  # TODO: add your code

        # save the predicted/simulated and realized/true next states
        x_sim_history.append(x_next_sim)
        x_history.append(x_next)

    # format data (for ease of plotting)
    x_sim_history = np.array(x_sim_history).T
    x_history = np.array(x_history).T

    # 2D trajectory plot
    plt.figure()
    plt.scatter(x0[0], x0[1], marker='x', c='red')
    plt.scatter(x_goal[0], x_goal[1], marker='*', c='green')
    plt.plot(x_sim_history[0, :], x_sim_history[1, :], color='blue', alpha=0.5, ls=':', lw='3')
    plt.plot(x_history[0, :], x_history[1, :], color='orange', alpha=0.5, ls='--', lw='2')
    plt.title('Robot Trajectory')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.legend(['start', 'goal', 'simulated', 'real'])
    plt.show()

    # plot x, y graphs
    t_hist = [t for t in range(t_max+1)]
    plt.subplot(211)
    plt.scatter(0, x0[0], marker='x', c='red')
    plt.scatter(t_max, x_goal[0], marker='*', c='green')
    plt.plot(t_hist, x_sim_history[0, :], color='blue', alpha=0.5, ls=':', lw='3')
    plt.plot(t_hist, x_history[0, :], color='orange', alpha=0.5, ls='--', lw='2')
    plt.plot(t_hist, x_goal[0]*np.ones([len(t_hist), 1]), color='black')

    plt.title('Dimension 1 trajectory')
    plt.legend(['start', 'goal', 'simulated', 'real', 'goal'])
    plt.subplot(212)
    plt.scatter(0, x0[1], marker='x', c='red')
    plt.scatter(t_max, x_goal[1], marker='*', c='green')
    plt.plot(t_hist, x_sim_history[1, :], color='blue', alpha=0.5, ls=':', lw='3')
    plt.plot(t_hist, x_history[1, :], color='orange', alpha=0.5, ls='--', lw='2')
    plt.plot(t_hist, x_goal[1] * np.ones([len(t_hist), 1]), color='black')
    plt.title('Dimension 2 trajectory')
    plt.legend(['start', 'goal', 'simulated', 'real', 'goal'])
    plt.show()


if __name__ == "__main__":
    main()
