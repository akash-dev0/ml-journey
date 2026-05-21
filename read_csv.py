import pandas as pd
import numpy as np

df = pd.read_csv("practice.csv")
print(df)
print(df.shape)
print(df[df["city"] == "Delhi"])
print(df[df["age"]>21])
df["senior"] = np.where(df["age"]>=23, "Yes", "No")
print(df)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df[["name", "score"]]) #select multiple columns 
df = df.rename(columns = {"score" : "marks", "city" : "location"}) #renaming columns
print(df)
df = df.drop(columns=["senior"]) #You're saying — "drop it, then save the result back into df."
print(df)
