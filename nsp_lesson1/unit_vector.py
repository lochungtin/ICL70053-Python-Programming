import numpy as np

x = np.array([3, 5, 1, 2, 4])
length = np.sqrt(np.square(x).sum())
unit_x = x / length

print(unit_x)
print(np.array([0.40451992, 0.67419986, 0.13483997, 0.26967994, 0.53935989]))
