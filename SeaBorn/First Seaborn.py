import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

table  = pd.read_csv('SeaBorn\dm_office_sales.csv')
# plt.figure(figsize=(12, 4), dpi= 200)
sns.scatterplot(x= 'salary', y= 'sales', data= table, hue= 'level of education')
plt.show()
print(table.head())