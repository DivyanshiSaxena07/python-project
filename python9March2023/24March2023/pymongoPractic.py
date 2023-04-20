from pymongo import MongoClient
myclient=MongoClient("mongodb+srv://divyanshitout:tout@cluster0.pr0hpr5.mongodb.net/?retryWrites=true&w=majority")
db=myclient.get_database('mydatabase')
records=db.myfirstCollection
val={
    'name':'mahi',
    'roll_no':'101',
    'branch':'it'
}
# print(records.insert_one(val))
# print(records.find_one('_id'))
# print(records.count_documents({}))

# print(myclient.list_database_names())

# remove duplicates 
mylist=["a","b","a","c","d"]
mylist=list(dict.fromkeys(mylist))
print(mylist)