# Problem: Compare KNN with and without scaling.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)

model1 = KNeighborsClassifier(n_neighbors=3)
model1.fit(X_train, y_train)
print("Without scaling:", accuracy_score(y_test, model1.predict(X_test)))

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model2 = KNeighborsClassifier(n_neighbors=3)
model2.fit(X_train_scaled, y_train)
print("With scaling:", accuracy_score(y_test, model2.predict(X_test_scaled)))
