from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.DataFrame({
    'Age': [20, 25, 30, 35, 40]
})

scaler = StandardScaler()
df['Age_Standardized'] = scaler.fit_transform(df[['Age']])

print(df)