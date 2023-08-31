import timeit

setup_code = """
import pandas as pd
import numpy as np 


table = pd.read_csv("Pandas/titanic_train.csv")

def typeOfPeople(Boggy, age, gender, live):
    parsonality = ''
    
    match Boggy:
        case 1:
            parsonality += "Amir, "
            
        case 2:
            parsonality += "Middle, "
            
        case 3:
            parsonality += "Garib, "
            

    if 0<age<12:
        parsonality += "Chhote Bacche, "
    
    if 12<age<18:
        parsonality += "Yonngester, "
    
    if 18<age<40:
        parsonality += "Adult, "
    
    if age < 12:
        parsonality += "Seniors, "

    match gender :
        case "female":
            parsonality += "Female, "
        case "male":
            parsonality += "Male, "

    if live:
        parsonality += "Jinda"
    else:
        parsonality += "No More"

    return parsonality
"""

method1 = '''table["Discription"] = table[["Pclass", "Age", "Sex", "Survived"]].apply(lambda table : typeOfPeople(table['Pclass'], table['Age'], table['Sex'], table['Survived']), axis= 1)'''
method2 = '''table["Discription"] = np.vectorize(typeOfPeople)(table['Pclass'], table['Age'], table['Sex'], table['Survived'])'''

r1 = timeit.timeit(setup= setup_code, stmt= method1, number= 1000)
print("Time taken by labmda Method : ", r1)

r2 = timeit.timeit(setup= setup_code, stmt= method2, number= 1000)
print("Time taken by vectorize Method : ", r2)