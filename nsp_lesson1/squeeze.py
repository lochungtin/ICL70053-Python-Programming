import numpy as np

x = np.array([[[1, 2]], [[3, 4]], [[5, 6]]])
print(x.shape)
print(x)

simpler_x = x.squeeze()
print(simpler_x)
print(np.array([[1, 2], [3, 4], [5, 6]]))
print(simpler_x.shape)
print((3, 2))
