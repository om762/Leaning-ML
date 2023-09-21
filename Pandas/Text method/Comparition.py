import timeit 

# code snippet to be executed only once 
setup = '''
import pandas as pd
import numpy as np
messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
def cleanup(name):
    name = name.replace(";","")
    name = name.strip()
    name = name.capitalize()
    return name
'''

# code snippet whose execution time is to be measured 
stmt_pandas_str = ''' 
messy_names.str.replace(";","").str.strip().str.capitalize()
'''

stmt_pandas_apply = '''
messy_names.apply(cleanup)
'''

stmt_pandas_vectorize='''
np.vectorize(cleanup)(messy_names)
'''

t1 = timeit.timeit(setup = setup, 
                    stmt = stmt_pandas_str, 
                    number = 10000) 

t2 = timeit.timeit(setup = setup, 
                    stmt = stmt_pandas_apply, 
                    number = 10000) 

t3 = timeit.timeit(setup = setup, 
                    stmt = stmt_pandas_vectorize, 
                    number = 10000) 

print("Time taken by String Method : ", t1)
print("Time taken by Apply Method : ", t2)
print("Time taken by Vectorize Method : ", t3)

'''
OUTPUT:
Time taken by String Method :  2.8913241000009293
Time taken by Apply Method :  1.0413159999989148
Time taken by Vectorize Method :  0.21591900000203168
'''