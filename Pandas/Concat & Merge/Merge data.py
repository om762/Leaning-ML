import pandas as pd

registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print(registrations)
print("\n\n\n")
print(logins)

merge_table = pd.merge(registrations, logins, how= "inner", on= 'name')
print("\n\n\n")
print(merge_table)