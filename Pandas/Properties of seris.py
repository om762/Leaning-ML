import pandas as pd 

table = pd.read_csv("Richest Persons.csv")
print(table)
print("Table Information")
print("Column are", table.columns)

print()

print(table.describe())