import matplotlib.pyplot as plt
import numpy as np

resolution = 1000
x = np.linspace(0, 50, resolution)
y = np.sin(x)
z = np.exp(y)

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, y, "b")
ax[1].plot(x, z, "r")

plt.show()
