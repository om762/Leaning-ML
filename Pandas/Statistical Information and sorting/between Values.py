import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")

print("These are the following passenger of age from 18 to 25")

print(table[table["Age"].between(18,25, inclusive= "both")]["Name"])
