import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

dataset = load_iris()

x = dataset.data
y = dataset.target
cat = dataset.target_names
ft = dataset.feature_names


# plt.figure()
# plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Set1, edgecolors="k")
# plt.xlabel(ft[0].capitalize())
# plt.ylabel(ft[1].capitalize())
# plt.show()


# plt.figure()
# plt.scatter(x[:, 2], x[:, 3], c=y, cmap=plt.cm.Set1, edgecolor="k")
# plt.xlabel(ft[2].capitalize())
# plt.ylabel(ft[3].capitalize())
# plt.show()


# fig, ax = plt.subplots(1, 3)

# ax[0].hist(x[y == 0, 2], color="r")
# ax[0].set(title=cat[0])

# ax[1].hist(x[y == 1, 2], color="g")
# ax[1].set(title=cat[1])

# ax[2].hist(x[y == 2, 2], color="b")
# ax[2].set(title=cat[2])

# plt.show()
# plt.close()


# df = pd.DataFrame(x)
# df.columns = ft

# fig = plt.figure(figsize=(8, 8))
# ax = fig.gca()
# df[y == 0][ft[2:4]].hist(ax=ax)

# plt.show()
