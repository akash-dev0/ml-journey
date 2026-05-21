import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Carlos", "Diana", "Eve"],
    "score": [85, np.nan, 90, np.nan, 78],
    "city": ["Delhi", "Mumbai", None, "Chennai", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df2 = df.dropna()
print(df2)
df["score"] = df["score"].fillna(df["score"].mean())
print(df)
df["city"] = df["city"].fillna("Unknown")
print(df)