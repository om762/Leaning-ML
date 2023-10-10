import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

table = pd.read_csv('SeaBorn\dm_office_sales.csv')
print(table.info())

sns.rugplot(x= 'salary', data= table, height= 0.7)
plt.show()