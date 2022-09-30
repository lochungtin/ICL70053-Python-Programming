from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

dataset = load_iris()

x = dataset.data
y = dataset.target

x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.20, random_state=42)

print(len(x_tr), len(y_tr))
print(len(x_ts), len(y_ts))

knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
knn.fit(x_tr, y_tr)

pred = knn.predict(x_ts)
prob = knn.predict_proba(x_ts)
print(pred)
print(prob)

score = accuracy_score(y_ts, pred)
print(score)

c_mat = confusion_matrix(y_ts, pred)
print(c_mat)

report = classification_report(y_ts, pred)
print(report)
