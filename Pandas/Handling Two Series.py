import pandas as pd

myMark10 = [78, 87, 91, 91, 90]
mySubjects10 = ['English', 'Hindi', 'Maths', 'Science', 'Social Science']

myMark12 = [87, 89, 85, 95, 89]
mySubjects12 = ['English', 'Computer Science', 'Maths', 'Chemistry', 'Physics']

MarkSheet10 = pd.Series(dict(zip(mySubjects10,myMark10)))
MarkSheet12 = pd.Series(dict(zip(mySubjects12,myMark12)))

# print(MarkSheet10)
# print()
# print(MarkSheet12)

# print(MarkSheet10+MarkSheet12)

# print(MarkSheet10 * MarkSheet12)

Total_of_both = MarkSheet10.add(MarkSheet12,fill_value = 0)
print(Total_of_both)