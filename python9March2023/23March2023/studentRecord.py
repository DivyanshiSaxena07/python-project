import mysql.connector as c
import emojis
mydb=c.connect(
    host='localhost',
    user='root',
    password='password',
    database='pythondatabase'
)
mycursor=mydb.cursor()

def school_name():    
    print("*****************************************************************************")
    print(emojis.encode("\t\t\t:school:Vaishnav Higher Sec. School\t\t\t"))
    print("*****************************************************************************")
print("\n Our services")
print("___________________")


def new_record():
    school_name()
    # mycursor.execute("create table student_info(Name varchar(30),Father_name varchar(30),DOB varchar(10),Address varchar(20),PhoneNo int(20))")
    name=input("Enter your name:\n")
    fatherName=input("Enter your father's name:\n")
    dob=input("Enter your date of birth:\n")
    address=input("Enter your address:\n")
    phoneNo=int(input("Enter your phone number:\n")) 
    query="insert into student_info values('{}','{}','{}','{}',{},{})".format(name,fatherName,dob,address,phoneNo,"NULL")
    mycursor.execute(query)
    mydb.commit()
    print("*************************************************")
    print(emojis.encode("\n:boom:Congratulation!!!!your data has been submitted:boom:\n"))
    print("*************************************************")
    print("Name:\t\t",name)
    print("Father's Name:\t",fatherName)
    print("DateOfBirth:\t",dob)
    print("Address:\t",address)
    print("PhoneNo:\t",phoneNo)
    
    
      
def view_record():
    school_name()
    print("\nInformation of all student\n")
    mycursor.execute("select * from student_info")
    for i in mycursor:
        print(i)
      
      
def search_record():
    school_name()
    rollNo=int(input("Enter Roll Number\n"))
    mycursor.execute(f"select * from student_info where rollNo={rollNo}") 
    for i in mycursor:
     print(i)     
     
     
def update_record():
    school_name()
    rollNo=input("Enter roll number which u want udate record")
    name=input("Enter your name:\n")
    fatherName=input("Enter your father's name:\n")
    dob=input("Enter your date of birth:\n")
    address=input("Enter your address:\n")
    phoneNo=int(input("Enter your phone number:\n")) 
    mycursor.execute(f"update student_info set Name='{name}',Father_name='{fatherName}',DOB='{dob}',Address='{address}',PhoneNo='{phoneNo}' where rollNo={rollNo}")     
    mydb.commit()
    print(mycursor.rowcount,"record updated!")
    
    
def remove_record():
    school_name()
    rollNo=int(input("Enter roll number which u want to delete records"))
    mycursor.execute(f"delete from student_info where rollNo={rollNo}")
    mydb.commit()
    print(mycursor.rowcount,"record deleted")
    
    
while True:     
    print(emojis.encode("\n\t1-:clipboard:New addimision\n\t2-:eyes:View all records\n\t3-:mag:Search records\n\t4-Remove records\n\t5-Update record\n\t6-exit"))
    ch=input("Enter your choice:\t")   
    if ch=='1':
        new_record()
    elif ch=='2':
        view_record()
    elif ch=='3':
        search_record()
    elif ch=='4':
        remove_record()
    elif ch=='5':
        update_record()
    elif ch=='6':
        print("Thank you for visiting!")
        exit()