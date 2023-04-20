import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='password',
    database='pythondatabase'
)
mycursor=mydb.cursor()
sql='update student set rollNo=101 where rollNo=102'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'row effected')