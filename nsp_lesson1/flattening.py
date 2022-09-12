import numpy as np

x = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [-6, -5, -4, -3]])

flattened_x = x.flatten()

print(flattened_x)
print(np.array([0, 1, 2, 3, 4, 5, 6, 7, -6, -5, -4, -3]))
