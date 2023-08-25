import pandas as pd
mydata = [78, 87, 91, 91, 90]
myindex = ['English', 'Hindi', 'Maths', 'Science', 'Social Science']

mySeries = pd.Series(data= mydata, index= myindex)

print(mySeries)
print("My Marks in Social Science : ", mySeries['Social Science'])