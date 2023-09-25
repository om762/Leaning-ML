import pymysql as sql
import pandas as pd
import numpy as np

data_base = sql.connect(host= "localhost", 
                        user= "root",
                        passwd= "Om762")

df = pd.DataFrame(data=np.random.randint(low=0, high=100, size= (4,4)),columns=['a', 'b', 'c', 'd'])
df.to_sql(name="Random Table", con=data_base, if_exists="replace")

Result = pd.read_sql_query(sql="Select * from Random Table", con=data_base)
print(Result)