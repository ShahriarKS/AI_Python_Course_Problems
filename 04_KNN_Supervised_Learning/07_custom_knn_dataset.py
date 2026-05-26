# Problem: KNN classification using custom dataset.
from sklearn.neighbors import KNeighborsClassifier

# Features: [study_hours, attendance]
X = [[2, 60], [3, 65], [8, 90], [9, 95], [1, 50], [7, 85]]
y = [0, 0, 1, 1, 0, 1]  # 0 = Fail, 1 = Pass

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

new_student = [[6, 80]]
print("Prediction:", "Pass" if model.predict(new_student)[0] == 1 else "Fail")
