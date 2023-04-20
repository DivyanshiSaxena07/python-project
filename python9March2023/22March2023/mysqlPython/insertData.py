import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    
    password='password',
    database='pythondatabase'
)
mycursor=mydb.cursor()
# single row inserted
# mycursor.execute('insert into student(rollNo,name,marks)values(101,"mahi",78)')
# multiple row inserted
sql="insert into student(rollNo,name,marks)values(%s,%s,%s)"
val=[
    (102,'mohini',89),
    (103,'mehul',85),
    (104,'sheelam',90)
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,'record inserted')
