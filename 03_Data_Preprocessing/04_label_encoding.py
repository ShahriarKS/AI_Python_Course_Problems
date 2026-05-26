# Problem: Apply Label Encoding.
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({"City": ["Dhaka", "Chittagong", "Dhaka", "Sylhet"]})
encoder = LabelEncoder()
df["City_Label"] = encoder.fit_transform(df["City"])

print(df)
