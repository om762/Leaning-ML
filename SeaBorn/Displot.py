import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

table = pd.read_csv('SeaBorn\dm_office_sales.csv')
print(table.info())

sns.set(style = 'darkgrid')
sns.kdeplot(data=table,x='work experience')
sns.displot(data=table,x='salary',kde=True, bins= 25, color='red', edgecolor= 'black', rug= True, linewidth= 2)
plt.show()