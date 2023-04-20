import mysql.connector as c 
mydb=c.connect(
    host='localhost',
    user='root',
    password='password',
    database='pythondatabase'
)
mycursor=mydb.cursor()
sql="select * from student limit 2"
mycursor.execute(sql)
for m in mycursor:
 print(m)