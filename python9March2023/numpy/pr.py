# import numpy as np
# l = [10,20,30,40]
# a = np.array([10,20,30,40])
# print(a)
 
# import numpy as np
# l=[20,43,13,24,23]
# a=np.array([10,20,30,40])
# print(a)


# --------------------------------------------------------------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# r=requests.get("https://finance.yahoo.com/most-active")
# soup=BeautifulSoup(r.content,'html.parser')
# s=soup.find('div',id="Lead-5-ScreenerResults-Proxy").find_all('tr')
# # print(soup.prettify())
# # print(r.content)
# # print(s)
# for line in s:
#     print(line.text," ") 


# import numpy as np

# arr = np.array([[3, 2, 4], [5, 0, 1]])

# print(np.sort(arr))


# ------------------------------------------------------------------------------------------------------

# import numpy as np
# arr=np.array([2,1,3,2,5])
# print(np.sort(arr))

# ------------------------------------------------------------------------------------------------------
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)#it will return index number

# ------------------------------------------------------------------------------------------------------

# import numpy as np

# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 8)

# print(x)

# ------------------------------------------------------------------------------------------------------
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='left')
y = np.searchsorted(arr, 7, side='right')
print(x)
print(y)

