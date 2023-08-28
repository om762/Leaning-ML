import pandas as pd
table = pd.read_csv('Student-info.csv')

table['Total Sum'] = (table['english.grade'] + table['math.grade'] + table['sciences.grade'] + table['language.grade'])*5

name_and_percent = table[['name', 'Total Sum']]
print(name_and_percent)