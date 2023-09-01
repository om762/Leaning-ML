import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")

myMap = {"female" : "F",  "male" : "M"}

table = table["Sex"].map(myMap)
print(table)