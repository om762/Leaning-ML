import pandas as pd

table = pd.read_csv("Pandas\Pivot Table\Sales_Funnel_CRM.csv")
lic = table[['Company', 'Licenses', 'Product']]
lic_pivot = lic.pivot(index='Company', columns='Product', values='Licenses')
print(lic_pivot)
