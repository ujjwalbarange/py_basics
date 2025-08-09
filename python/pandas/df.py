import pandas
df1=pandas.DataFrame([[2,3,4],[10,20,30]], columns=["a","b","c"], index=["a","b"])
print(df1.mean().mean())