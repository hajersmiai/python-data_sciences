# %%
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


folder = Path(__file__).parent
file= Path(folder,"social_network_data.csv")
df=pd.read_csv(file)

count=df["friends"].value_counts()
plt.bar(count.index,count)
plt.show()
# %%
print(df.sort_values(by=["friends","minutes"], ascending = False))
print(max(df["friends"]))
# %%
df_filtred=df[df["friends"]<100]
print(df_filtred.mean())
# %%
print(df.median())
print(df_filtred.median())
# %%
print(df.quantile(0.5))
print(df.quantile(0.75))
# %%
print(max(df["friends"]))
print(min(df["friends"]))
print(max(df["minutes"]))
print(min(df["minutes"]))
# %%
print(df.var())
print(df_filtred.var())
# %%
print(df.std())
print(df_filtred.std())
# %%
print(df.describe())
# %%
print(df.head(3))
print(df.tail(5))
# %%
print(df.cov())
# %%
print(df.corr())
# %%
plt.scatter(df_filtred["friends"],df_filtred["minutes"])
coeff = np.polyfit(df_filtred["friends"],df_filtred["minutes"],1)
p=np.poly1d(coeff)
x=np.linspace(0,50,100)
plt.plot(x,p(x),"r-")
plt.show()
# %%
