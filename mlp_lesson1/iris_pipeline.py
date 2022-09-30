from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.svm import SVC

dataset = load_iris()

x = dataset.data
y = dataset.target

x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.20, random_state=42)


pipeline = Pipeline([("s", StandardScaler()), ("m", MinMaxScaler()), ("c", SVC())])

pipeline.fit(x_tr, y_tr)
pred = pipeline.predict(x_ts)

print(accuracy_score(y_ts, pred))

res_dict = cross_validate(pipeline, x_tr, y_tr, cv=5)
print(res_dict.keys())
print(res_dict["test_score"])
print(res_dict["test_score"].mean())
