import numpy as np

x = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [-6, -5, -4, -3]])

reshaped_x = x.reshape((2, 6), order="f")

print(reshaped_x)
print(np.array([[0, -6, 5, 2, -4, 7], [4, 1, -5, 6, 3, -3]]))
