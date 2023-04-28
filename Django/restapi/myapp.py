import requests
import json
# URL="http://127.0.0.1:8000/stuinfo"

# data = {
#     'name':'Sonam',
#     'roll':101,
#     'city':'Ranchi'
# }
# json_data = json.dumps(data)
# # r=requests.get(url=URL)
# r=requests.get(url=URL, data=json_data)
# data= r.json()
# print(data)

def get_data(id=None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r=requests.get(url="http://127.0.0.1:8000/stuinfo", data=json_data)
    data= r.json()
    print(data)
    
# get_data(2)

def post_data():
    data = {
        'roll':106,
        'name':'Sonam',
        'subject':'Btech',
        'age':'23'
    }
    json_data = json.dumps(data)
    r=requests.pidost(url="http://127.0.0.1:8000/stuinfo", data=json_data)
    data= r.json()
    print(data)
    
    
def update_data():
    data = {'id': 3, 'name': 'manshi', 'roll': 10}
    jdata = json.dumps(data)
    r = requests.put(url="http://127.0.0.1:8000/stuinfo", data=jdata)
    data = r.json()
    print(data)
# Run

def delete_data():
    data={'id':3}
    json_data = json.dumps(data)
    r=requests.delete(url="http://127.0.0.1:8000/stuinfo", data=json_data)
    data=r.json()
    print(data)

delete_data()
# update_data()
    
# post_data()