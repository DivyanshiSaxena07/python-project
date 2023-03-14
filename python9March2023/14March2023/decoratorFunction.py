# def decorator(func):
#  def inner(name):
#   if name=="Sunny":
#    print("Hello Sunny Bad Morning")
#   else:
#    func(name)
#  return inner 
# @decorator
# def wish(name):
#  print("Hello",name,"Good Morning")
# wish("Durga")
# wish("Ravi")
# wish("Sunny")

# def zeroDivision(func):
#     def inner(a,b):
#         if b==0:
#          print("Number can not be divided by zero")
#         else:
#          return func(a,b)
#     return inner

# @zeroDivision

# def opration(a,b):
#     print(a/b)
# opration(10,5)
# opration(10,0)

# def check(func):
#     def inner(age):
#         if age<18:
#             print("Oops! your age is lesser than 18 you are not eligible to vote")
#         else:
#             return func(age)
#     return inner
# @check
# def vote(age):
#     print("Only equal to 18 and greter than 18 are eligible")
# vote(18)
# vote(17)


# def decor(func):
#  def inner(name):
#   if name=="Sunny":
#    print("Hello Sunny Bad Morning")
#   else:
#     func(name)
#  return inner
# def wish(name):
#  print("Hello",name,"Good Morning")
# decorfunction=decor(wish)
# wish("Durga") #decorator wont be executed
# wish("Sunny") #decorator wont be executed
# decorfunction("Durga")#decorator will be executed
# decorfunction("Sunny")#decorator will be executed


# def decor(func):
#  def inner(name):
#   print("First Decor(decor) Function Execution")
#   func(name)
#  return inner
# def decor1(func):
#  def inner(name):
#   print("Second Decor(decor1) Execution")
#   func(name)
#  return inner
# @decor
# @decor1
# def wish(name):
#  print("Hello",name,"Good Morning")
# wish("Durga")

# g=[x*x for x in range(0,10)]
# print(g)

# g=(x*x for x in range(0,10))
# while True:
#  print(next(g))

import random
import time

names=['Sunny','Hunny','Bunny']
subjects=['python','java','c']

# def listPerson(num):
#     result=[]
#     for i in range(num):
#         person={
#             'id':i,
#             'name':random.choice(names),
#             'subject':random.choice(subjects)
#         }
#         result.append(person)
#     return result
# # t1 = time.clock()
# people =listPerson(10)
# print(people)
# # t2 = time.clock()
# # print('Took {}'.format(t2-t1))



def people_generator(num_people):
 for i in range(num_people): 
  person = {
        'id':i,
        'name': random.choice(names),
        'major':random.choice(subjects)
  }
  yield person
  people = people_generator(10)
  print(people)
