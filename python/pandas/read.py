import pandas
df1=pandas.read_csv("csvf.csv", header=None)
df1.columns = ["name","roll"]
df1=df1.set_index("name")
print(df1)