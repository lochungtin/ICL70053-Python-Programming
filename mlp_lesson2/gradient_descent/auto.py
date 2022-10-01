import torch


def gradient_descent_torch_autograd(initial_theta, learning_rate, number_steps):
    """
    Args:
        initial_theta (torch.Tensor): Initial value of theta
        learning_rate (float)
        number_steps (int): number of 1-step gradient descent to perform.

    Returns:
        final_theta (torch.Tensor): Final value of theta after multiple 1-step gradient descents with automatic gradient.
    """
    for i in range(number_steps):
        grad = torch.nn.Parameter(initial_theta)
        loss = grad * grad
        loss.backward()

        initial_theta -= learning_rate * grad.grad

    return initial_theta


initial_theta = torch.Tensor([1])
print(
    gradient_descent_torch_autograd(initial_theta, learning_rate=0.2, number_steps=20)
)
