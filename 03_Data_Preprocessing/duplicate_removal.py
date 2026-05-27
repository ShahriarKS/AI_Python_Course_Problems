import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'John'],
    'Age': [22, 25, 22, 30]
})

print("Before:")
print(df)

df = df.drop_duplicates()

print("\nAfter:")
print(df)