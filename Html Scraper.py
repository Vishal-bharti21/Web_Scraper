from bs4 import BeautifulSoup
import os
import pandas as pd

d={'title':[],'price':[],'link':[]}

for file in os.listdir("data"):
    try:
        with open (f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc,'html.parser')
        t =soup.find("h2")
        title = t.get_text()
       

        l = t.find("a")
        link = "https://amazon.in/"+ l['href']
        p =soup.find("span",attrs={"class": 'a-price-whole'})
        price = p.get_text()
        
        print(title,price)
        d['title'].append(title)
        d['link'].append(link)
        d['price'].append(price)
    except Exception as e:
        print(e)

df=pd.DataFrame(data=d)
df.to_csv("data.csv")