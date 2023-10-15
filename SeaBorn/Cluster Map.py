import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2020 Projections
df = pd.read_csv('SeaBorn\country_table.csv')
df = df.set_index('Countries')
print(df)


rates = df.drop('Life expectancy',axis=1)
# sns.clustermap(rates,linewidth=2,annot=True,cmap='viridis')
sns.clustermap(rates,col_cluster=False,figsize=(12,8),cbar_pos=(-0.1, .2, .03, .4), cmap='viridis')
plt.show()
