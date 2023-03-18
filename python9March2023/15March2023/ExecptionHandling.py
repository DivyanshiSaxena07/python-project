# Syntax Errror 
# x=10
# if x==10
#   print("hello")

# print(10/0)
# print("Hiii numbers")
# try:
#  print(10/"ten")
# except Exception as e:
#     print("integer can not be divided by string",e)
# finally:
#     print("Programe execution succesful!")
# print("Task complete")


# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second Number: "))
#     print(x/y)
# except ZeroDivisionError :
#     print("Can't Divide with Zero")
# except ValueError:
#     print("please provide int value only")


# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second Number: "))
#     print(x/y)
# except Exception :
#     print("Can't Divide with Zero")
# except ValueError:
#     print("please provide int value only")
    
    
# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second Number: "))
#     print(x/y)

# except ValueError:
#     print("please provide int value only")
# except Exception :
#     print("Can't Divide with Zero")



# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second Number: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as msg:
#     print("Plz Provide valid numbers only and problem is: ",msg)



# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except:
#     print("Default Except")


# try:
#  print(10/0)
# except:
#  print("Default Except")
# except ZeroDivisionError:
#  print("ZeroDivisionError")



# import os
# try:
#  print("try")
#  os._exit(-12)
# except NameError:
#  print("except")
# finally:
#  print("finally")




# import os
# try:
#  print("try")
#  os._exit()
# except NameError:
#  print("except")
# finally:
#  print("finally")




# import os
# try:
#  print("try")
#  os._exit(12)
# except NameError:
#  print("except")
# finally:
#  print("finally")




# import os
# try:
#  print("try")
#  os._exit(0)
# except NameError:
#  print("except")
# finally:
#  print("finally")



# import os
# try:
#  print("try")
#  os._exit("ten")
# except NameError:
#  print("except")
# finally:
#  print("finally")


# import os
# ten=10
# try:
#  print("try")
#  os._exit(ten)
# except NameError:
#  print("except")
# finally:
#  print("finally")


# try:
#  print("try")
# except :
#  print("except-1")
# else:
#  print("else")


# try:
#  print("try")
# else:
#  print("else")


# try:
#  print("try")
# finally :
#  print("except-1")
# else:
#  print("else")


# try:
#  print("try")
# except :
#  print("except-1")
# else:
#  print("else")
# else:
#  print("else2")

# try:
#     print("try")
# except:
#     print("except")
# try:
#     print("try2")
# except:
#     print("except2")
    
    
    
# try:
#     print("try")
# except:
#     print("except")
# try:
#     print("try2")
# finally:
#     print("finally")
    
    
    
# class TooYoungException(Exception):
#  def __init__(self,arg):
#   self.msg=arg
  
  
# class TooOldException(Exception):
#  def __init__(self,arg):
#   self.msg=arg
  
# age=int(input("Enter Age:"))
# if age>60:
#  raise TooYoungException("Plz wait some more time you will get best match soon!!!")
# elif age<18:
#  raise TooOldException("Your age already crossed marriage age...no chance of getting marriage") 
# else:
#  print("You will get match details soon by email!!!")



# import logging
# logging.basicConfig(filename='log.txt',level=logging.WARNING)
# print("Logging Module Demo")
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")


# import logging
# logging.basicConfig(filename='mylog.txt',level=logging.INFO)
# logging.info("A New request Came:")
# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second Number: "))
#     print(x/y)
# except ZeroDivisionError as msg:
#  print("cannot divide with zero")
#  logging.exception(msg)
# except ValueError as msg:
#  print("Enter only int values")
#  logging.exception(msg)
# logging.info("Request Processing Completed")


def squareIt(x):
 return x*x
assert squareIt(2)==4,"The square of 2 should be 4"
assert squareIt(3)==9,"The square of 3 should be 9"
assert squareIt(4)==16,"The square of 4 should be 16"
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))