import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")

print(table.sample())

print("\n\n\n")
print(table.sample(5))

print("\n\n\n")
print("1% of data frame")
print(table.sample(frac= 0.01))