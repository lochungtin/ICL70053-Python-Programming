import torch


def logistic(tensor):
    """
    Args:
        tensor (torch.Tensor)

    Return:
        logistic_tensor (torch.Tensor) : resulting tensor after having applied the logistic function to all elements of tensor.
    """
    return 1 / 1 + torch.exp(-1 * tensor)
