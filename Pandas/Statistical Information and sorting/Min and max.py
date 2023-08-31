import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")

print("The Oldest person  on the train",table['Age'].max(),"\n\n")
indexOfMax = table['Age'].idxmax()
print("The information of oldest person  on train : \n")
print(table.iloc[indexOfMax], '\n\n')


print("The youngest person  on the train",table['Age'].min(),"\n\n")
indexOfMin = table['Age'].idxmin()
print("The information of youngest person  on train : \n")
print(table.iloc[indexOfMin])