# Problem: Apply One Hot Encoding.
import pandas as pd

df = pd.DataFrame({"Color": ["Red", "Blue", "Green", "Red"]})
encoded = pd.get_dummies(df, columns=["Color"])

print(encoded)
