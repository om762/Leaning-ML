import pandas as pd

table = (pd.read_csv("Student-info.csv")).head(10)
table = table[['name', 'nationality', 'city', 'age']]
print(table)

table = table.set_index('name')

print(table)
# print(table['Rochelle Johnson'])

table.reset_index(inplace = True)
print(table)
