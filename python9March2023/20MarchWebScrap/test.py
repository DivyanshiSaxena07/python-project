import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.bookswagon.com/book/lifes-amazing-secrets-gaur-gopal/9780143442295")
print(r)
# print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

s = soup.find('div', class_="container mt-2 pt-3 pb-1 product-detailwrapper")
 
lines = s.find_all('p')
 
for line in lines:
    print(line.text)


# import requests
# from bs4 import BeautifulSoup
# r=requests.get("https://www.bookswagon.com/book/lifes-amazing-secrets-gaur-gopal/9780143442295")
# soup=BeautifulSoup(r.content,'html.parser')
# # print(soup.find('div', class_="container mt-2 pt-3 pb-1 product-detailwrapper"))
# for line in soup.find_all('p'):
#     print(line.text)



# import requests
# from bs4 import BeautifulSoup as bs
# import csv

# URL = 'https://www.geeksforgeeks.org/page/'
# req=requests.get(URL)

# soup = bs(req.text, 'html.parser')

# titles = soup.find_all('div', attrs={'class', 'head'})
# titles_list = []

# count = 1
# for title in titles:
# 	d = {}
# 	d['Title Number'] = f'Title {count}'
# 	d['Title Name'] = title.text
# 	count += 1
# 	titles_list.append(d)

# filename = 'titles.csv'
# with open(filename, 'w', newline='') as f:
# 	w = csv.DictWriter(f,['Title Number','Title Name'])
# 	w.writeheader()
	
# 	w.writerows(titles_list)
