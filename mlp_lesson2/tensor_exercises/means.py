import torch


def mean_tensors(tensors_list):
    """
    Args:
        tensors_list (List[torch.Tensor]) list of tensors of the same shape

    Return:
        mean_tensors (torch.Tensor) : resulting tensor after having calculated the mean of all tensors passed as input.
    """
    length = len(tensors_list)
    assert length > 0
    return sum(tensors_list) / length
