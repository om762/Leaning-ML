import pandas as pd

table = pd.read_csv("Pandas\\Row Column Manipulation\\Student-info.csv")
table = table.head(15)

StudentOfUSA = table['nationality'] == "United States of America"

print(StudentOfUSA)
StudentOfUSA = table[StudentOfUSA]
print(StudentOfUSA)