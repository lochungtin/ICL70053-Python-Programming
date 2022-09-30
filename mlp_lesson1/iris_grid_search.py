import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier

dataset = load_iris()

x = dataset.data
y = dataset.target

x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.20, random_state=42)

grid = {
    "n_neighbors": np.arange(1, 51),
    "metric": ["manhattan", "euclidean", "chebyshev"],
}

knn = GridSearchCV(KNeighborsClassifier(), cv=10, param_grid=grid)
knn.fit(x_tr, y_tr)

print(knn.best_params_)
print(knn.best_score_)

pred = knn.best_estimator_.predict(x_ts)
print(accuracy_score(y_ts, pred))
