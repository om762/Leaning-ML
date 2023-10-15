import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2020 Projections
df = pd.read_csv('SeaBorn\country_table.csv')
df = df.set_index('Countries')
print(df)


rates = df.drop('Life expectancy',axis=1)
sns.heatmap(rates,linewidth=2,annot=True,cmap='viridis')
plt.show()
