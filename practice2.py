import pandas as pd
import numpy as np

data = {
    "employee": ["Amit", "Sara", "Raj", "Priya", "Karan"],
    "department": ["HR", "IT", "IT", "HR", "Finance"],
    "salary": [45000, 80000, 75000, 50000, 90000],
    "age": [28, 35, 30, 26, 40]
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.info())
print(df[df["salary"]>60000])
df["senior"] = np.where(df["age"]>=30 , "Yes" , "No")
print(df)
print(df.groupby("department")["salary"].mean())
df = df.drop(columns=["age"])
print(df)
"C:\Users\ss\Downloads\PANDAS"