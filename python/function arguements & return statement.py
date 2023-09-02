# Function arguements in python
def average(a,b):
    print("The average is" , (a+b)/2) 
average(4,6)
# default argument example:
def average(a=5,b=10):
    print ("The average is",(a+b)/2)
average()
# example #2
def name(name1,name2="hamza",name3= "riaz"):
    print("Hello,",name1,name2,name3)
name("fayyaz")
    #  we can change the name in the above line and interpreter will
    # prefer this names instead of those given in def name

    # variable lenght argument
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print("The average is",sum/ len(numbers))
average(6,10,4)
# return statement
# the return statement is used to return the value of the expression 
# back to the calling function 

# example#1:
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        return sum/ len(numbers)
c= average(9,9)
print(c)
# list methods in python

