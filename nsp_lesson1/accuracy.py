import numpy as np

x = np.array([[18, 3, 9], [1, 30, 4], [7, 5, 23]])

accuracy = x.diagonal().sum() / x.sum()

print(accuracy)
print(0.71)
