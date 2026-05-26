# Problem: Identify missing values in a dataset.
import pandas as pd

data = {"Age": [20, None, 22], "Score": [80, 90, None]}
df = pd.DataFrame(data)

print(df)
print("Missing values:
", df.isnull().sum())
