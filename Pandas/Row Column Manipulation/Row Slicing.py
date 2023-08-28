# Write a program to get data of row which are in a slice. That is use slicing to get the data of rows
import pandas as pd

table = (pd.read_csv("Student-info.csv"))
# table = table[['name', 'nationality', 'city', 'age']]


table.set_index('name', inplace = True)
data1 = table.iloc[5 : 10]



print("All information about index 5 to 10")
print(data1)