import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.geeksforgeeks.org/multiple-inheritance-in-python/")
soup=BeautifulSoup(r.content,'html.parser')
s=soup.find('div',class_="a-wrapper")
for line in s:
    print(line.text) 
