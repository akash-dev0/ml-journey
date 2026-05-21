import pandas as pd 

s = pd.Series([10,20,30,40])
print(s)

data = {
    "name" : ["Alice", "Bob", "Carlos"],
    "score" : [85,72,90]
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.columns)
print(df["name"])
print(df[df["score"] > 80])
df["passed"] = df["score"] > 80
print(df)

df["city"]= ['Delhi','Mumbai', 'Delhi']
print(df)
df["age"] = [20,25,22]
print(df)