import numpy as np

x = np.random.random_sample((10, 8, 5))
y = np.random.random_sample((10, 5))

new_y = y[:, np.newaxis, :]

z = x + new_y
print(z)
