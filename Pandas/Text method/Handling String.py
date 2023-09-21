import pandas as pd

names = pd.Series(['andrew','bobo','claire','david','4'])
print(names.str.capitalize())
print("\n\n")
print(names.str.isdigit())