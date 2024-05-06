import requests as rq
import json
import matplotlib.pyplot as plt
import pandas as pd


response =rq.get('https://www.frankfurter.app/2024-03-21..?to=USD')
data=json.loads(response.text)
# print (data)
rates=data['rates']
# print(rates)
all_val=[]
all_date=[]

for date,val in rates.items():
    all_val.append(val['USD'])
    all_date.append(pd.to_datetime(date))


d=pd.DataFrame({"Date": all_date,"USD":all_val})

plt.plot(d["Date"],d["USD"],'b.-')
plt.xlabel('Date')
plt.ylabel('Rate')
plt.show()