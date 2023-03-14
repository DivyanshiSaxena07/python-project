# def myFunction():
#     print("hello")

# myFunction()

# def add(a,b):
#     print("Addition:",a+b)
# def multiply(a,b):
#     print("Multiply:",a*b)
# def subtract(a,b):
#     print("Subtraction:",a-b)
# def divide(a,b):
#     print("Division:",a/b)

# add(10,39)
# multiply(12,30)
# divide(30,10)
# subtract(30,12)


# Arbitory Argument 
# def myFunction(*name):
#     print(name)
# myFunction("rohit","sima","nayan")

# Keyword Argument
# def myFunction(first,second,third):
#     print(first," ",second," ",third)
    
# myFunction(second="himani",first="mahi",third="sonal")

# Arbitory Keyword Argument
# def myFunction(**name):
#     print(name)
# myFunction(first="hello",second="this",third="is",fourth="me")

# Default Argument
# def myFUnction(country="India"):
#     print(country)
    
# myFUnction("Norway")
# myFUnction()

# Passing a list as an argument
# def listArgumnet(food):
#     print(food)
# fruits=["Mango","Apple","Banana"]
# listArgumnet(fruits)


# passing a tuple as an argumnet
# def listArgumnet(food):
#     print(food[1])
# fruits=("Mango","Apple","Banana")
# listArgumnet(fruits)

# return value
# def myFunction(x):
#     return 5*x
# print(myFunction(3))


# Recursion 

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(5)


# Even odd

# def evenOdd(num):
#     if num%2==0:
#         print("Number is even")
#     else:
#         print("Number is odd")
# evenOdd(13)

# Factorial

# def factorial(num):
#  fact=1
#  while num>0:
#      fact=fact*num
#      num=num-1
#  print(fact)
# factorial(5)

# Return any number of value in python
# def sub_sum(a,b):
#     sub=a-b
#     sum=a+b
#     return sub,sum
# x,y=sub_sum(10,20)
# print(x)
# print(y)
 
 
#  Q. Write a Python Function to find factorial of given number with recursion.

# def factorial(n):
#  if n==0:
#     result=1
#  else:
#     result=n*factorial(n-1)
#  return result
# print("Factorial of 4 is :",factorial(4))
# print("Factorial of 5 is :",factorial(5))

# Q. Write a program to create a lambda function to find square of given number?
# s=lambda n:n*n
# print("The Square of 4 is :",s(4))
# print("The Square of 5 is :",s(5))

# Q. Lambda function to find sum of 2 given numbers
# sum=lambda a,b:a+b
# print("Sum of 2 number is: ",sum(3,8))

# Q. Lambda Function to find biggest of given values.
# max=lambda a,b:a if a>b else b
# print("Biggest number is",max(40,54))


# max=lambda a,b,c:a if a>b and a>c else b if b>a and b>c else c
# print("Biggest number is",max(40,54,64))

# filter function
# l=[0,5,10,15,20,25,30]
# l1=list(filter(lambda x:x%2==0,l))
# print(l1) #[0,10,20,30]
# l2=list(filter(lambda x:x%2!=0,l))
# print(l2) #[5,15,25]

# l=[0,2,3,4,5,7,6,8,9]
# l1=list(filter(lambda x:x%2==0,l))
# print(l1)


# l=[0,2,3,4,5,7,6,8,9]
# l1=filter(lambda x:x%2==0,l)
# print(l1) #<filter object at 0x7fe22431ea30>


# l=[0,2,3,4,5,7,6,8,9]
# l1=set(filter(lambda x:x%2==0,l))
# print(l1)

# map
# l=[2,3,4,5,6,7,8]
# l1=list(map(lambda x:x*2,l))
# print(l1)#[4, 6, 8, 10, 12, 14, 16]

# l=[2,3,4,5,6,7,8]
# l1=list(map(lambda x:x%2==0,l))
# print(l1)#[True, False, True, False, True, False, True]

# Eg 2: To find square of given numbers
# sq=[2,3,4,5,6,7]
# sqr=list(map(lambda x:x*x,sq))
# print(sqr)
# from functools import *
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x*y,l)
# print(result) #12000000

# Function aliasing
# def wish(name):
#     print("good morning",name)
# greeting=wish
# greeting("divyanshi")
# wish("divya")


# Nested Function 
# def outer():
#     a="hello"
#     def inner():
#      b=10
#      print(a)
     
#     inner()

# outer()


# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
# g=mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
z=9
def firstn(num):
 n=1
 while n<=num:
  yield n
  n=n+1
values=firstn(5)
for x in values:
  print(x)