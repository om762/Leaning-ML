import pandas as pd

table = (pd.read_csv("Student-info.csv")).head(10)
print(table)

#axis is use to decide what should be drop a row or column when axix = 0 that denote row axis = 1 denote columns
#inplce will change the main table
#Either we can use table = table.drop(...)
table.drop([2, 4, 6], axis= 0, inplace= True)
print(table)