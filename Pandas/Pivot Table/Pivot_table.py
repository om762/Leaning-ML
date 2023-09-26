import pandas as pd

table = pd.read_csv("Pandas\Pivot Table\Sales_Funnel_CRM.csv")

pivot_table = table.groupby('Company').sum()
# pivot_table = pd.pivot_table(data=table, index='Company', aggfunc='sum')
print(pivot_table)
pivot_table.to_csv('Pandas\Pivot Table\TO WATCH.csv')