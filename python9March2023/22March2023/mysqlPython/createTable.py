import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='pythondatabase'
)
mycursor=mydb.cursor()
mycursor.execute('create table student(rollNo int,name varchar(20),marks int)')
mycursor.execute('desc student')
for t in mycursor:
    print(t)
print("Table created")