import pandas
datset = pandas.read_csv("cc.csv", header=0)
print(datset.mean())