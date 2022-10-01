def single_step_gradient_descent(theta, learning_rate):
    """
    Args:
        theta (float)
        learning_rate (float)

    Returns:
        new_theta (float): updated value of theta after 1 step of gradient descent.
    """
    return theta - 2 * theta * learning_rate


def gradient_descent(initial_theta, learning_rate, number_steps):
    """
    Args:
        initial_theta (float): Initial value of theta
        learning_rate (float)
        number_steps (int): number of 1-step gradient descent to perform.

    Returns:
        final_theta (float): Final value of theta after multiple 1-step gradient descents
    """
    for i in range(number_steps):
        initial_theta = single_step_gradient_descent(initial_theta, learning_rate)

    return initial_theta


theta = gradient_descent(1, 0.2, 20)
print(theta)
