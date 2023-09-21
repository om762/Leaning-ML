import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")
table = table.groupby("Pclass").mean('Fare')
print(table)
