import pandas as pd
import numpy as np

data = {
    "name": ["Rahul", "Priya", "Aman", "Sneha"],
    "subject": ["Math", "Science", "Math", "Science"],
    "marks": [88,76,95,60]
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df[df["marks"]>80])
df["result"] = np.where(df["marks"] >= 75, "Pass", "Fail") #np.where works like this:
                    #if condition is True → give first value, else → give second value
print(df)


print(df["name"])
print(df[df["subject"] == "Math"])
df['bonus'] = df["marks"] + 5
print(df)


import pandas as pd

data = {
    "product": ["Laptop", "Phone", "Tablet", "Earphones"],
    "price": [55000, 15000, 20000, 2000],
    "quantity": [10, 25, 8, 50]
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
df["total_value"] = df["price"] * df["quantity"]
print(df)
print(df["product"])
print(df[df["price"]>10000])

df["country"] = "India"
print(df)
