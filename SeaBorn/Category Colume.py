import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

table = pd.read_csv('SeaBorn\dm_office_sales.csv')
print(table.value_counts('level of education'))

plt.figure(figsize=(10, 4))
sns.countplot(data= table, x= 'division', hue= 'division', palette='prism')
plt.show()