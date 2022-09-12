import numpy as np

a = np.array([[2, 4], [3, -2]])
b = np.array([8, 8])
x = np.linalg.inv(a) @ b

print(x)
print(np.array([3.0, 0.5]))
