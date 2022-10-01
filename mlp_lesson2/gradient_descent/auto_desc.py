import torch


def gradient_descent_torch_optimiser(initial_theta, learning_rate, number_steps):
    """
    Args:
        initial_theta (torch.Tensor): Initial value of theta
        learning_rate (float)
        number_steps (int): number of 1-step gradient descent to perform.

    Returns:
        final_theta (torch.Tensor): Final value of theta after several gradient descents performed with the SGD torch optimiser.
    """
    tensor = torch.nn.Parameter(initial_theta, requires_grad=True)
    optimiser = torch.optim.SGD(params=[tensor], lr=learning_rate)

    for i in range(number_steps):
        optimiser.zero_grad()
        loss = torch.sum(tensor * tensor)
        loss.backward()

        optimiser.step()

    return tensor


initial_tensor = torch.Tensor([1, -1])
print(
    gradient_descent_torch_optimiser(initial_tensor, number_steps=20, learning_rate=0.2)
)
