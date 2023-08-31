import pandas as pd 

table = pd.read_csv("Pandas\Richest Persons.csv")

'''
def simple(num):
    return num*2
'''
function = lambda value : value / 10000000

result = table['networth'].apply(function)
print(result)