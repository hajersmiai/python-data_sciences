from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as p



url ='https://www.scrapethissite.com/pages/simple/'
response = rq.get(url)

soup= bs(response.text, 'html5lib')

titles = []
capitales=[]
areas=[]
populations=[]


for element in soup.find_all("div", class_="country") :
     t = element.find("h3").text.strip()
     titles.append(t)
     c = element.find("span", class_="country-capital").text.strip()
     capitales.append(c)
     d = element.find("span", class_="country-area").text.strip()
     areas.append(float(d))
     r = element.find("span", class_="country-population").text.strip()
     populations.append(r)

df= p.DataFrame({'Country': titles, 'Capital': capitales, 'Area': areas, 'Populations': populations})
print (df)