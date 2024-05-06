import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime 

url="https://api.frankfurter.app/2024-03-01..?to=USD"
response =requests.get(url)
data = json.loads(response.text)
# print(data.keys())
all_dates=[]
all_rates=[]
rates = data["rates"]
for date, rate in rates.items():
    all_dates.append(datetime.datetime.strptime(date,"%Y-%m-%d"))
    # all_dates.append(pd.to_datetime(date)) **2ème méthode**
    all_rates.append(rate["USD"])
df = pd.DataFrame({"Date": all_dates, "USD": all_rates})

plt.plot(df["Date"], df["USD"],'b.-')
plt.xlabel("Date")
plt.ylabel("Rates")
plt.show()