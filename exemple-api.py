import requests 
import json


response =requests.get("https://official-joke-api.appspot.com/random_joke")

data=json.loads(response.text)
print (type(response.text))
print(type(data))
print(data["setup"])