import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")
table.sort_values(['Age', 'Name'], inplace= True, ascending= True )
print(table[['Age', 'Name']].iloc[250 : 260])