# Problem: Split dataset into train and test set.
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.DataFrame({"Hours": [1,2,3,4,5], "Marks": [40,50,60,70,80]})
X = df[["Hours"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train:
", X_train)
print("X_test:
", X_test)
