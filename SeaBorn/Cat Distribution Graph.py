import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

table = pd.read_csv('SeaBorn\StudentsPerformance.csv')
print(table.head())

plt.figure(figsize=(12,6))
sns.boxplot(x='parental level of education',y='math score',data=table, hue= 'parental level of education')


plt.figure(figsize=(12,6))
sns.violinplot(x='parental level of education',y='math score',data=table,hue='gender')

plt.figure(figsize=(12,6))
sns.violinplot(x='parental level of education',y='math score',data=table,inner='stick', hue='parental level of education')


plt.figure(figsize=(12,6))
sns.swarmplot(x='race/ethnicity',y='math score',data=table,hue='gender',dodge=True)

plt.show()