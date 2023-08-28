import pandas as pd

table = pd.read_csv("Pandas\\Row Column Manipulation\\Student-info.csv")

StudentOfUSA = table[(table['nationality'] == 'United States of America') & (table['gender'] == 'M')]
print(StudentOfUSA)