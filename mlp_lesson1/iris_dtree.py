from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

dataset = load_iris()

x = dataset.data
y = dataset.target

x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.20, random_state=42)

print(x_tr.shape)
print(y_tr.shape)

dt1 = DecisionTreeClassifier(criterion="entropy", random_state=10)
dt1.fit(x_tr, y_tr)

dt2 = DecisionTreeClassifier(criterion="gini", random_state=10, max_depth=2)
dt2.fit(x_tr, y_tr)

pred1 = dt1.predict(x_ts)
print("D Tree 1")
print(accuracy_score(y_ts, pred1))
print(confusion_matrix(y_ts, pred1))

pred2 = dt2.predict(x_ts)
print("D Tree 2")
print(accuracy_score(y_ts, pred2))
print(confusion_matrix(y_ts, pred2))
