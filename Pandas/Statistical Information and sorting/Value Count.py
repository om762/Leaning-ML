import pandas as pd

table = pd.read_csv("Pandas/titanic_train.csv")

print("The Status of life")
print(table['Survived'].value_counts())

print("\nMale Female ratio :")
print(table["Sex"].value_counts())

print("\nPeople of Class")
print(table["Pclass"].value_counts())

