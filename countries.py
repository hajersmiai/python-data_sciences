import numpy as np
import pandas as pd
from pathlib import Path as p
import matplotlib.pyplot as plt

# df=pd.read_csv("countries.csv")
# print(df)
#  les 2 fichiers countries.csv et countries.py doivent ètre dans le meme répertoire
file_path = p(__file__).parent
print(file_path.parent)
df = pd.read_csv(p(file_path, "countries.csv"))
print(df)

d= pd.DataFrame(df)
print(d)
x=d['Name']
y=d['Population']


plt.ylabel('Population')
plt.xlabel('Country')

plt.plot(x,y)

plt.show()