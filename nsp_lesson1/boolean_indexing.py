import numpy as np

data = np.array(
    [
        [5.46, 3.06],
        [2.08, 1.57],
        [7.28, 3.06],
        [3.35, 4.74],
        [2.51, 2.43],
        [3.91, 4.55],
        [2.72, 3.11],
        [6.05, 2.72],
        [0.84, 3.57],
        [1.14, 6.31],
    ]
)

label = np.array([1, 2, 1, 2, 2, 2, 1, 1, 2, 2])

data_1 = data[label == 1].T
data_2 = data[label == 2].T

print(data_1)
print(np.array([[5.46, 7.28, 2.72, 6.05], [3.06, 3.06, 3.11, 2.72]]))

print(data_2)
print(
    np.array(
        [[2.08, 3.35, 2.51, 3.91, 0.84, 1.14], [1.57, 4.74, 2.43, 4.55, 3.57, 6.31]]
    )
)