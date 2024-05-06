from bs4 import BeautifulSoup
import requests as rq


url="https://www.scrapethissite.com/pages/simple/"
response=rq.get(url)

soup = BeautifulSoup(response.text, "html5lib")

# # for paragraph in soup.find_all("h1"):
#  print(paragraph)

title= soup.find("h1")
txt=title.text.strip()

while "  " in txt:
    txt = txt.replace("  "," ")
print(txt) 