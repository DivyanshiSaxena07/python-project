import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password'
)
print("connected!!!")
mycursor=mydb.cursor()
# mycursor.execute("create database pythondatabase")
mycursor.execute('show databases')
for x in mycursor:
 print(x)