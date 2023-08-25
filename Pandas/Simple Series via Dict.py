import pandas as pd

mydata = [78, 87, 91, 91, 90]
myindex = ['English', 'Hindi', 'Maths', 'Science', 'Social Science']

myDict = dict(zip(myindex, mydata))
mySeries = pd.Series(myDict)

print(mySeries)
print("My Marks in Social Science : ", mySeries['Social Science'])