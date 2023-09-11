import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")
print(table.groupby(["Pclass", "Embarked"]).mean("pfj"))

