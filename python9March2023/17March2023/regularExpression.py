import re
# patern=re.compile('python')
# print(type(patern))

# count=0
# pattern=re.compile('ab')
# matcher=pattern.finditer("abaababa")
# for m in matcher:
#     count=count+1
#     print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
# print(count)
    
    
    
# count=0
# matcher=re.finditer('ab',"abaababa")
# for m in matcher:
#     count=count+1
#     print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
# print(count)


# import re
# matcher=re.finditer('[a-z]','abcsysy765@')
# for m in matcher:
#     print(m.start(),"=",m.group())
    

    
# import re
# matcher=re.finditer('[a-z]','abcsysy2728@')
# for m in matcher:
#     print(m.start(),"=",m.group())    
    
    
    
# import re

# string="hello world "
# pattern="world"
# match=re.search(pattern,string)
# if match:
#     print("Match found!")
# else:
#     print("Match is not found")




# import re
 
# string = "The quick brown fox jumps over the lazy dog."
# pattern = r"brown.fox"
 
# match = re.search(pattern, string)
# if match:
#     print("Match found!",pattern)
# else:
#     print("Match not found.")
   
   
   
# import re
# number=input("Enter nunber")
# regex='\d+'
# match =re.findall(regex,number)
# if match:
#     print("Contact number is:",match)
# else:
#     print("Pls enter valid number, number must be 10 digit") 
    
    
# import re
# number=input("Enter ")
# regex=r'[0-9]'
# match=re.findall(regex,number)
# print(match)

# import re
# n=input("Enter number:")
# m=re.fullmatch("[7-9]\d{9}",n)
# if m!= None:
#   print("Valid Mobile Number")
# else:
#   print("Invalid Mobile Number")



import re,urllib
# import urllib.request
# sites="google rediff".split()
# print(sites)
# for s in sites:
#     print("Searching...",s)
#     u=urllib.request.urlopen("http://"+s+".com")
#     text=u.read()
#     title=re.findall("<title>.*</title>",str(text),re.I)
#     print(title[0])
    
    
    
    
import re
s=input("Enter Mail id:")
m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m!=None:
 print("Valid Mail Id");
else:
 print("Invalid Mail id")