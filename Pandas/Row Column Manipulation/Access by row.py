import pandas as pd

table = (pd.read_csv("Student-info.csv"))
# table = table[['name', 'nationality', 'city', 'age']]


table.set_index('name', inplace = True)
data1 = table.iloc[5]
data2 = table.loc['Joshua Lonaker']


print("All information about index 5 and Joshua Lonaker")
print(data1)
print(data2)