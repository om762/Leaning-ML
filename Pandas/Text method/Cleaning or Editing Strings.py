import pandas as pd

messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
'''0      andrew  
1         bo;bo
2      claire  
dtype: object'''
messy_names.str.replace(";", "",)
'''0      andrew  
1          bobo
2      claire  
dtype: object'''
messy_names.str.strip()
'''0    andrew
1     bo;bo
2    claire
dtype: object'''
messy_names.str.capitalize()

messy_names = messy_names.str.replace(";","").str.strip().str.capitalize()
print(messy_names)