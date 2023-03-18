# class Demo:
#  def __init__(self,name,rollno,marks):
#    self.name=name
#    self.rollno=rollno
#    self.marks=marks
            
#  def talk(self):
#     print("What is ur name:",self.name)
#     print("my rollno is:",self.rollno)
#     print("i got marks:",self.marks)
    
# d=Demo("Mahi",20,80)
# d.talk()


# Constructor

# class Test:


#  def __init__(self):

#   print("Constructor exeuction...")
  
#  def m1(self):
#    print("Method execution...")
   
# t1=Test()
# t2=Test()
# t3=Test()
# t1.m1()


# class Student:
    

#     def __init__(self,x,y,z):
#         self.name=x
#         self.rollno=y
#         self.marks=z
#     def display(self):
#         print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self.marks))

# s1=Student("Divyansh",101,80)
# s1.display()
# s2=Student("Sohil",102,100)
# s2.display()


class Employee:

 def __init__(self):

  self.eno=100

  self.ename='Dheera'

  self.esal=10000
e=Employee()
print(e.__dict__)