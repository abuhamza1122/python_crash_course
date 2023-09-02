# break statement in pyhton 
for i in range(12):
    print("5 X",i+1,"=",5*i)
    if(i==10):
        break
print("skip the loop")
# continue statement in python
for i in range (12):
    if(i==10):
      print("skip the iteration")
      continue
print("5 X",i+1,"=",i*5)
# Functions in python
# a function is a block of code that performs a specific task whenever it is called
# example#1
# a = 9
# b=8
# gmean1 =( a*b)/(a+b)
# print(gmean1)
# and 
c =4
d =5
gmean2=(c*d)/(c+d)
print(gmean2)
# so we will use function to make our work easier:the same above examples 
def calculategmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
a=7
b=8
calculategmean(a,b)
# now, for the same example 2 
def gmean(c,d):
    mean=(c*d)/(c+d)
    print(mean)
c=10
d=12
gmean(c,d)
def islesser(a,b):
    pass
# the above example shows the use of "pass" function that implies that
# the function is incomplete and we can use it to run another function 
# without getting error 


