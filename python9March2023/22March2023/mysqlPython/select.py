import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='password',
    database='pythondatabase'
)
mycursor=mydb.cursor()
mycursor.execute("select * from student")
# myresult=mycursor.fetchall()
myresult=mycursor.fetchone()
print(myresult)
# for i in myresult:
#     print(i)