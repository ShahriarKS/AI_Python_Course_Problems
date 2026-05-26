# Problem: Normalize data using Min-Max scaling.
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({"Salary": [10000, 20000, 50000, 80000]})
scaler = MinMaxScaler()
df["Salary_Normalized"] = scaler.fit_transform(df[["Salary"]])

print(df)
