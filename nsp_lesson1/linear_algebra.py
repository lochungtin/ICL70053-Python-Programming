import numpy as np

x = np.array([[1, 2, 3], [2, 4, 5]])
y = np.array([3, 5])
w = (x.T @ x) @ x.T @ y

print(w)
print(np.array([767, 1534, 2001]))
