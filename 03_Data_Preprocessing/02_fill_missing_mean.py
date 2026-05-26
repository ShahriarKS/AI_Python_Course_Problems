# Problem: Fill missing numerical values using mean.
import pandas as pd

df = pd.DataFrame({"Age": [20, None, 22, 25], "Score": [80, 90, None, 70]})

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

print(df)
