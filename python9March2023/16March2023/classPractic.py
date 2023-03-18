

# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.c=30
# t=Test()
# t.m1()
# t.d=30
# t.d="hello"
# print(t.__dict__)



# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def display(self):
#         print(self.a)
#         print(self.b)
# t=Test()
# t.display()
# print(t.a,t.b)


# class Test:

#     def __init__(self):
#         self.a=10

#         self.b=20
    
#         self.c=30
    
#         self.d=40
   
#     def m1(self):
   
#       del self.d
   
# t=Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# del t.c
# print(t.__dict__)



# class Test:
#     x=10
#     def __init__(self):
#         self.y=20
# t1=Test()
# t2=Test()
# print('t1:',t1.x,t1.y)
# print('t2:',t2.x,t2.y)
# Test.x=345
# t1.y=354
# print('t1:',t1.x,t1.y)
# print('t2:',t2.x,t2.y)


# class Test:
#     a=10
#     def __init__(self):
#         Test.b=20
#     def m1(self):
#         Test.c=30
#     def m2(cls):
#         cls.d1=40
#         Test.d2=400
#     def m3():
#         Test.e=50
# print(Test.__dict__)

# t=Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__)
# Test.m2("hello")
# print(Test.__dict__)
# Test.m3()
# print(Test.__dict__)
# Test.f=60
# print(Test.__dict__)


# class Demo:
#     def __init__(name):
#         name.en="mahi"
#         name.ea=40
#         name.task()
        
#     def task(name):
#         print(name.en)
#         print(name.ea)

# d=Demo()



# class Student:
#     def setName(self,name):
#         self.name=name
        
#     def getName(self):
#         return self.name
    
#     def setMarks(self,marks):
#         self.marks=marks
        
#     def getMarks(self):
#         return self.marks
    
# n=int(input("Enter number of students:"))
# for i in range(n):
#     s=Student()
#     name=input("Enter Name:")
#     s.setName(name)
#     marks=int(input("Enter Marks:"))
#     s.setMarks(marks)
    
#     print("Heyy",s.getName())
#     print("You Marks are:",s.getMarks())
#     print()
        
        
# Static method

# class Demo:
#     st = "jhd  sahsdlah ahdslah "
    
#     def __init__(self,name,age):
#         self.name
    
#     def add(x,y):
#         print("Sum:",x+y)
    
    
#     def product(x,y):
#         print("Multiply:",x*y)
        
# Demo.add(2,3)


class Person:
    def __init__(self):
        self.name='diya'
        self.db=self.Dob()
    def display(self):
     print('Name:',self.name)
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1947
        def display(self):
         print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
p=Person()
p.display()
x=p.db
x.display()


