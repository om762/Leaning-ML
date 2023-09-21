import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")


table["Age"].fillna(table["Age"].mean(), inplace= True)

print("Average Age of passengers : ", table["Age"].mean())
table["Age"] = table["Age"].round(2)
print(table.sample(10))
