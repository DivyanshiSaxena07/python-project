import requests,json
from bs4 import BeautifulSoup
r=requests.get("https://www.bookswagon.com/search-books/books")
print(r)

def getData():
    soup=BeautifulSoup(r.text,'html.parser')
    s = soup.find('div', class_="product").findAll('div',class_='product-summary')
    bookName,author,publisher,price,release,language,status=[],[],[],[],[],[],[]  
    for l in s:
        bookName.append(l.find('div',class_='title').find('a').get_text())
        author.append(l.find('div',class_="author-publisher").find('a').get_text())
        publisher.append(l.find('div',class_="author-publisher").find('a').get_text())
        price.append(l.find('div',class_="price-attrib").find('div',class_='price').find('div',class_='sell').text)
        release.append(l.find('div',class_='attributes').find('div',class_='attributes-title').text)
        language.append(l.find('div',class_='attributes').find('div',class_='attributes-title').text)
        # status.append(l.find('div',class_='list-view-books').find('div',class_="action").find('div',class_='available-stock').text)
        print(language)
    dict={}
    list1=[]
    for a,b,c,d,e,f in zip(bookName,author,publisher,price,release,language):
        dict["bookName"]=a
        # j=j[1:5]
        # j=int(j)
        dict["author"]=b
        dict["publisher"]=c
        dict["price"]=d
        dict["release"]=e
        dict["language"]=f
        # dict["status"]=g 
        list1.append(dict.copy())
    fp=open("scrap.json","w")
    json.dump(list1,fp,indent=4)
    fp.close()
    return(dict)
demo=getData()     
# print(demo)       
   
        
            
            
            
        
        