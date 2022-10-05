# Introduction to Deep Learning with PyTorch

## Ch3 Tensor

- **Initialisation**
	- From list
		- `torch.Tensor([1, 2], [3, 4])`
	- From numpy array
		- `torch.from_numpy(np.array([1, 2], [3, 4]))`
	- Like numpy
		- `torch.zeros(size=shape)` / `zeros_like(tensor)`
		- `torch.ones(size=shape)` / `ones_like(tensor)`
		- `torch.randn(size=shape)` / `rand_like(tensor)`
- **Mathematical operations**
	- `+`, `*` - element to element operation
- `.item()`
	- Torch object to python type
- `.view(*shape)`
	- `-1` shape flattens the tensor
	- **Shallow copies** original tensor
- Supports **slicing**

## Ch4 PyTorch for Automatic Gradient Descent

- `torch.nn.Parameter`
	- Tensor with gradient
	- `.backward()`
		- Computes loss
- `optim` module
	- Optimiser
		- `torch.optim.SGD(params=thetas, lr=...)`
	- `.zero_grad()`
		- Reset tensor gradient to 0
	- `.step()`
		- One update step
