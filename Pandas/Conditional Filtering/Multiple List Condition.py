import pandas as pd

table = pd.read_csv("Pandas\\Row Column Manipulation\\Student-info.csv")

Student = table['nationality'].isin(['Japan', 'Mexico'])
Student = table[Student]
print(Student)