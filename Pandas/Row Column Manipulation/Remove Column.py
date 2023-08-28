#Write a program to remove a row and column form a DataFrame using pandas

import pandas as pd

table = pd.read_csv("Student-info.csv")
print(table)

#axis is use to decide what should be drop a row or column when axix = 0 that denote row axis = 1 denote columns
#inplce will change the main table
#Either we can use table = table.drop(...)
table.drop(['nationality','city','latitude','longitude','gender'], axis= 1, inplace= True)
print(table)