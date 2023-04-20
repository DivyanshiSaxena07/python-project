# State and their capitals
import requests,json
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
r=requests.get("https://www.safalta.com/blog/list-of-states-in-india#list")

def state_info():
    soup=BeautifulSoup(r.content,'html.parser')
    s=soup.find('div',class_='bg-white mt-1').find_all('div',class_='story-body ul_styling')
    state,capital,founded=[],[],[]
    for i in s:
        state.append(i.find('td').text)
        capital.append(i.find('strong')[i].text)
        print(capital)
    dict={}
    list=[]
    for i,j in zip(state,capital):
        dict['state']=i
        dict['capital']=j
        list.append(dict.copy())
    f=open("state.json",'w')
    json.dump(state,f,indent=4)
    f.close()
    return(dict)
     
tabel=Table(title='State and their Capitals')
fr=open('state.json','r')
data=json.load(fr)
tabel.add_column("State",justify='right',style='cyan',no_wrap=True)
tabel.add_column("Capital",style='magenta')
tabel.add_column("Founded",justify='right',style='green')     
for i in data:
    tabel.add_row(i)
console=Console()
console.print(tabel)
state_info()