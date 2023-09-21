import pandas as pd
import numpy as np

table = pd.read_csv("Pandas/titanic_train.csv")

bool_table = table.notnull()
table= table[bool_table]
print(table.head(10))