import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")

print("The ten most aged passenger are")
print(table.nlargest(10, "Age"))

print("\n\nThe ten most young passeners are")
print(table.nsmallest(10, "Age"))