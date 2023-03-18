# class Dog:
#     def talk(self):
#         print("Bow Bow ")
        
#     def talk(self):
#         print("Moew Moew")

# d=Dog()
# d.talk()


# class Dog:
#     def talk(self):
#         print("Bark")
# class Cat:
#     def talk(self):
#         print("Moew Moew")

# def f1(obj):
#     obj.talk()
# l=[Dog(),Cat()]
# for obj in l:
#  f1(obj)
 
 
# class Dog:
#     def talk(self):
#         print("Bark")
# class Cat:
#     def walk(self):
#         print("Moew Moew")

# def f1(obj):
#     obj.talk()
# l=[Dog(),Cat()]
# for obj in l:
#  f1(obj)



# class Duck:
#  def talk(self):
#     print('Quack.. Quack..')
# class Human:
#     def talk(self):
#         print('Hello Hi...')
# class Dog:
#  def bark(self):
#     print('Bow Bow..')
# def f1(obj):
#     if hasattr(obj,'talk'):
#      obj.talk()
#     elif hasattr(obj,'bark'):
#      obj.bark()
# d=Duck()
# f1(d)
# h=Human()
# f1(h)
# d=Dog()
# f1(d)



# class Book:
#     def __init__(self,pages):
#          self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
# b1=Book(100)
# b2=Book(200)
# print('The Total Number of Pages:',b1+b2)#300




# class Book:
#     def __init__(self,pages):
#          self.pages=pages
#     def __add__(self,other):
#         return self.pages*other.pages
# b1=Book(100)
# b2=Book(200)
# print('The Total Number of Pages:',b1+b2)#20000


# class Test:
#     def m1(self):
#      print('no-arg method')
#     def m1(self,a):
#        print('one-arg method')
#     def m1(self,a,b):
#       print('two-arg method')
# t=Test()
# t.m1(10,20)
# t.m1()


# class Test:
#     def sum(self,*a):
#         total=0
#         for x in a:
#             total=total+x
#         print('The Sum:',total)
# t=Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum(10)
# t.sum()



# class Test:
#     def __init__(self,a=None,b=None,c=None):
#         print("constructor calling.....")

# t1=Test()
# t2=Test(10)
# t3=Test(10,20)


# overriding

# class A:
#     def property(self):
#      print("hello")

# class B(A):
#     def marry(self):
#         print("hello guys")

# a=B()
# a.property()


# inheritance

# class Parent:
#     def property(self):
#         print("Parent class called")

# class Child(Parent):
#     def property2(self):
#         print("child class called")
        
        
# obj=Child()
# obj.property()
# obj.property2()



# class Mother:
#     mothername = ""
 
#     def mother(self):
#         print(self.mothername)
 

 
 
# class Father:
#     fathername = ""
 
#     def father(self):
#         print(self.fathername)
 

 
 
# class Son(Mother, Father):
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)
 
 

# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()


# class Grandfather:
#     def __init__(self,grandfathername):
#         self.grandfathername=grandfathername
        
        
# class Father(Grandfather):
#     def __init__(self,fathername,grandfathername):
#         self.fathername=fathername
        
#         Grandfather.__init__(self,grandfathername)
        
# class Son(Father):
#     def __init__(self,sonname,fathername,grandfathername):
#         self.sonname=sonname
        
#         Father.__init__(self,fathername,grandfathername)
        
#     def print_name(self):
#         print('Grandfather name:',self.grandfathername)
#         print("Father name:",self.fathername)
#         print("Son name:",self.sonname)
        
        
# s1=Son('Mehul','Vijay','Mahi')
# print(s1.grandfathername)
# s1.print_name()
        
        
class Parent:
    def fun1(self):
        print("Parent class")
        
        
        
class Child1(Parent):
    def fun2(self):
        print("Child1 class")
        
        
class Child2(Parent):
    def fun3(self):
        print("Child2 class")
        
        
object1 = Child1()
object2 = Child2()
object1.fun1()
object1.fun2()
object2.fun1()
object2.fun3()