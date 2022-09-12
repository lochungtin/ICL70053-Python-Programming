import numpy as np

x = np.array([3, 4, 1, 5])
y = np.array([4, 1, 1, -1])

len_x = np.sqrt(np.square(x).sum())
len_y = np.sqrt(np.square(y).sum())

unit_x = x / len_x
unit_y = y / len_y

angle_deg = np.rad2deg(np.arccos(np.dot(unit_x, unit_y)))

print(angle_deg)
print(67.32549258300477)
