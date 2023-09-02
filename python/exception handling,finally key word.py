# # EXCEPTION HANDLING IN PYTHON
# # DEMO:
# a = input("enter the number:")
# print(f"multiplication table of {a} is : ")
# for i in range(1,11):
#     print(f"{int(a)}X {i}={int (a)*i}")
# # now,imagine if we put a string as input instead of number...obviously the error will occur.so to tackle this 
# # error by:
# a = input("enter the number:")
# print(f"multiplication table of {a} is : ")
# try:
#   for i in range(1,11):
#     print(f"{int(a)}X {i}={int (a)*i}")
# except:
#    print("invalid input")

# print("try again")
# print("sorry for trouble")       #the code will excecute to end no matter the code is ok or not 

# # exception handling is the process of responding to unwanted or unexpected events when a computer program
# # runs.it deals with these event to prevent program or system crashing,otherwise,it will disrupt the system

# try:
#     num= int(input("enter an integar:"))
# except ValueError:
#     print("number entered is not an integar")
# # FOR MULTIPLE ERRORS : WE CAN USE MULTIPLE "except"
# try:
#    num1= int(input("enter a  number "))
#    a= [6,3]
#    print(a[num])
# except ValueError:
#    print("the number entered is not a postive number")
# except IndexError:
#    print("invalid number")










# FINALLY KEYWORD IN PYTHON
# It is also a part of exception handling which executes function what matter the code is ok or not
# DEMO:
def func1():
    try:
        l= [1,5,6,7]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")
x = func1()
print(x)
