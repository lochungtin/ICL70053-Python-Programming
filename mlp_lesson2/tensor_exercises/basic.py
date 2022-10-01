import torch

tensor = torch.Tensor([[1, 2], [3, 4]])
row_tensor = torch.Tensor([1, 2])
tensor_shape_3_2 = torch.Tensor([[1, 2], [3, 4], [5, 6]])

tensor_add = tensor + tensor
tensor_multiply = tensor * tensor
tensor_subtract = tensor - row_tensor

tensor_exp = torch.exp(tensor)
tensor_log = torch.log(tensor)

tensor_min = torch.min(tensor)
tensor_max = torch.max(tensor)
tensor_mean = torch.mean(tensor)

tensor_mean_row = torch.mean(tensor, dim=0)
tensor_mean_col = torch.mean(tensor, dim=1)

mean_item = tensor.mean().item()

t01 = torch.randn(size=(1, 4))
t02 = torch.randn(size=(2, 4))
concatenation0 = torch.cat(tensors=(t01, t02), dim=0)

t11 = torch.randn(size=(3, 1))
t12 = torch.randn(size=(3, 5))
concatenation1 = torch.cat(tensors=(t11, t12), dim=1)

print(tensor_add)
print(tensor_multiply)
print(tensor_subtract)

print(tensor_exp)
print(tensor_log)

print(tensor_min)
print(tensor_max)
print(tensor_mean)

print(tensor_mean_row)
print(tensor_mean_col)

print(mean_item, type(mean_item))

print(tensor_shape_3_2.size())
print(tensor_shape_3_2.shape)

print(concatenation0)
print(concatenation0.size())

print(concatenation1)
print(concatenation1.size())
