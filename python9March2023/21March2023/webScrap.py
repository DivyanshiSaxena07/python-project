import requests,json,csv
from bs4 import BeautifulSoup
url = "https://www.bookswagon.com/search-books/books"
res = requests.get(url)
def scrap_top_list():
    soup = BeautifulSoup(res.text,'html.parser')
    raw_html = soup.find("div",{"class":"product"}).findAll("div",class_="product-summary")
    bookName,author,price=[],[],[],
    for i in raw_html:
        bookName.append(i.find("div",{"class":"title"}).find("a").get_text())
        author.append(i.find("div",{"class":"author-publisher"}).find("a").get_text())
        price.append(i.find("div",{"class":"price-attrib"}).find("div",{"class":"price"}).find("div",{"class":"sell"}).text)
        ans=i.find("div",{"class":"attributes"}).find("table").find_all("td")
        li = []
        for rel in ans:
            relea=rel.find("div",{"class":"attributes-title"})
            if relea!=None: li.append(relea.text) 
        if len(li)==3:local_dict=({"Binding":li[0],"Release":li[1],"Language":li[2]})
        elif len(li)==2:local_dict=({"Binding":li[0],"Release":li[1]})
        else : local_dict=({"Binding":li[0]})

    dict = {}
    list1 = []
    for i,j,k in zip(bookName,author,price):
        dict["bookName"]=i
        dict["author"]=j
        dict["price"]=k
        dict.update(local_dict)
        list1.append(dict.copy())
    f = open("scraping11111.json",'w')
    json.dump(list1,f,indent=4)
    f.close()
    with open('titles.csv', 'w', newline='',encoding='utf-8') as f:
        w = csv.DictWriter(f,['bookName','author',"price","Release","Binding","Language"])
        w.writeheader()
        w.writerows(list1)
        
    return (list1) 
task = scrap_top_list()   
# =================================================================================================

