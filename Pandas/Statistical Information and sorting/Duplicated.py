import pandas as pd

table = pd.DataFrame([1,2,2,435,5,2,5,25], ["a", "b", "c", "d", "e", "f","g", "h"])
print(table.drop_duplicates())