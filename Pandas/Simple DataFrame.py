import numpy as np
import pandas as pd

np.random.seed(762)
marks = np.random.randint(50,101,(10,5))

Student = ['Omprakash', 'Vinayak', 'Kapil', 'Rishabh', 'Dhananjay', 'Vidit', 'Suresh', 'Maduri', 'Aastha', 'Chinmay']
Subjects = ['Physics', 'Chemistry', 'Computer Science', 'Maths', 'Bio']

result = pd.DataFrame(marks, Student, Subjects)
print(result)
print()
print(result.info())