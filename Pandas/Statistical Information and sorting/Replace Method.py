import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")
table["Sex"].replace(["female", "male"], ["F", "M"], inplace= True)
print(table)