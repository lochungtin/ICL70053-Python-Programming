import matplotlib.pyplot as plt
import numpy as np

resolution = 1000

x = np.linspace(0, 50, resolution)
y = np.sin(x)
z = np.exp(y)

plt.figure("My Graph")
plt.ylabel("Amplitude (W)")
plt.xlabel("Time (s)")

plt.plot(x, y)
plt.plot(x, z)

plt.legend(["y", "z"], loc="upper center")

plt.ylim([-0.5, 2.0])

plt.savefig("nsp_lesson1/graph_save.png")

plt.show()
