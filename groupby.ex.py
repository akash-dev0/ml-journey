import pandas as pd

data = {
    "salesman": ["Raj", "Priya", "Aman", "Sneha", "Vikram", "Neha"],
    "city": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", "Chennai"],
    "sales": [15000, 22000, 18000, 12000, 25000, 9000]
}

df = pd.DataFrame(data)
print(df)

# Which city made the most total sales?
print(df.groupby("city")["sales"].sum())

# Which city has the highest average sale per salesman?
print(df.groupby("city")["sales"].mean())

# How many salesmen per city?
print(df.groupby("city")["salesman"].count())