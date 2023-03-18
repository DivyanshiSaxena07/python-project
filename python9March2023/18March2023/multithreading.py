# from threading import*
# def display():
#     print("this code by thread:",current_thread().getName())
# t=Thread(target=display)
# t.start()


# import threading
# print("Current Executing Thread:",threading.current_thread().getName())


# from threading import*
# def display():
#     for i in range(1,10):
#         print("child thread called..")
# t=Thread(target=display) 
# t.start()
# for i in range(1,10):
#     print("Main Thread")



# from threading import*
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Child Thread-1")
# t=MyThread()
# t.start()
# for i in range(10):
#     print("Main Thread-1")

# from threading import*
# class Test:
#     def display(self):
#         for i in range(10):
#             print("Child Thread-2")
# obj=Test()
# t=Thread(target=obj.display)
# t.start()
# for i in range(10):
#     print("Main Thread-2")


# from threading import *
# import time
# def doubles(numbers):
#  for n in numbers:
#   time.sleep(1)
#   print("Double:",2*n)
# def squares(numbers):
#  for n in numbers:
#     time.sleep(1)
#     print("Square:",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# doubles(numbers)
# squares(numbers)
# print("The total time taken:",time.time()-begintime)


# from threading import *
# print(current_thread().getName())
# current_thread().setName("Pawan Kalyan")
# print(current_thread().getName())
# print(current_thread().name)


# from threading import *
# def test():
#  print("Child Thread")
# t=Thread(target=test)
# t.start()
# print("Main Thread Identification Number:",current_thread().ident)
# print("Child Thread Identification Number:",t.ident)


# from threading import *
# import time
# def display():
#  print(current_thread().getName(),"...started")
#  time.sleep(3)
#  print(current_thread().getName(),"...ended")
# t1=Thread(target=display,name="ChildThread1")
# t2=Thread(target=display,name="ChildThread2")
# t3=Thread(target=display,name="ChildThread3")
# t1.start()
# t2.start()
# t3.start()
# l=enumerate()
# for t in l:
#  print("Thread Name:",t.name)
# time.sleep(5)
# l=enumerate()
# for t in l:
#  print("Thread Name:",t.name)


from threading import *
import time
def display():
    for i in range(10):
        print("Seetha Thread")
        time.sleep(5)
t=Thread(target=display)
t.start()
t.join()#This Line executed by Main Thread
for i in range(10):
    print("Rama Thread")