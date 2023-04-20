from pymongo import MongoClient
client=MongoClient("mongodb+srv://divyanshitout:tout@cluster0.pr0hpr5.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database('mydatabase')
record=db.myfirstCollection
print("\n\t\t\t********************ABC College**********************")
def information():
        name=input("your name:")
        father_name=input("your father's name:")
        year=int(input("your 12th pass out year:"))
        per=int(input("your percentage:"))
        caste=input("your caste:")
        num=int(input("your contact number:"))
        address=input("your address:")
        
        val={
            'Name':name,
            'Father_name':father_name,
            'Year':year,
            'Percantage':per,
            'Caste':caste,
            'Phone_no':num,
            'Address':address      
        }
        x=record.insert_one(val)
        print("your student id is:",x.inserted_id)
        print("record inserted!")

def new_addmision():
    print("\n\t\tBCA\n\t\tBSC\n\t\tBTECH")
    ch=input("Enter course in which u take addmision:")
    if ch=='BCA':
        information()
       
        
        # print("\nBranch:-\n\tIT\n\tCS\n\tEC")
        
        
def view_record():
    x=record.find()
    for f in x:
        print(f)        

def search_record():
    name=input("Enter name:")
    x=record.find({'Name':name})
     
    for i in x:
            print(i)
   
def remove_record():
    name=input("Enter name:") 
    x=record.delete_one({'Name':name})  
    # for i in x:
    print(x,"record deleted!")
   

while True:
    print("\n\t\t1=>*New Addmision*\n\t\t2=>*View All Records*\n\t\t3=>*Search Record*\n\t\t4=>*Remove Record*\n\t\t5=>*Exit*")
    ch=input("Enter your choice:")
    if ch=='1':
        new_addmision()
    elif ch=='2':
        view_record()
    elif ch=='3':
        search_record()
    elif ch=='4':
        remove_record()
    elif ch=='5':
     print("Thank you for connecting!")
     exit()