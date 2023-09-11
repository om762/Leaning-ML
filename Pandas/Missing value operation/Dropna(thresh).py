import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")


table.dropna(axis= 0, inplace= True)
print(table)
