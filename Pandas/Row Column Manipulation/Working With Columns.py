import pandas as pd

result = pd.read_csv("Student-info.csv")
result = result.head(10)
print(result.describe())
print(result.columns)