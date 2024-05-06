import pandas as pd
import requests
import json

# df=pd.DataFrame([1,2,3])
# df.to_csv("test.csv")


url="https://api.frankfurter.app/2024-03-01..to=USD"
response=requests.get(url)
data= response.text

with open("dump.txt","w") as file:
    file.write(data)
    # file.close() avec with on n'a pas besoin de fermer le fichier car il se ferme dès qu'on sort de ce boucle

with open("dump.txt","r") as file:
    data =file.read()

    class Myclass:
        def __init__(self,number):
            self.number=number
       
        def __repr__(self):
            return f"Super objet Myclass avec number={self.number}"
        
        def __enter__(self):
            print ("Inside Enter!")
            return self
        def __exit__(self,*args):
            print(f"Inside Exit! {args}")
m=Myclass(5)
with Myclass(7) as truc:
    print (truc.number)

