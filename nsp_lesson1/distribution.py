import numpy as np

x = np.array([[18, 3, 9], [1, 30, 4], [7, 5, 23]])
distribution = x.sum(axis=1) / x.sum()

print(distribution)
print(np.array([0.3, 0.35, 0.35]))
