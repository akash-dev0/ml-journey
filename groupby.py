import pandas as pd

df = pd.read_csv("practice.csv")
print(df)
print(df.groupby("city")["score"].mean())
print(df.groupby("city")["score"].sum())
print(df.groupby("city")["age"].mean())