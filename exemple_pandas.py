import numpy as np
import pandas as pd

s= pd.Series([10,30,np.nan,40,62,18])
# print (s[2:4])

dates = pd.date_range('2019-07-09', periods=6, freq='h')
s=pd.Series([10,30,20,40,62,18],index=dates)
# print(s)

# data frame
rnd = np.random.randn(6,4)
df = pd.DataFrame(rnd,index=dates,columns=["A","B","C","D"])
# print (df.A)
# print(df[0:1])
# print(df[[True, False,False,True,False,False]])
print(df[df["A"]>0])


data ={
    "User": ["user1","user2","user4"],
    "Score": [15,7,0]
}
scores=pd.DataFrame(data)
print(scores)