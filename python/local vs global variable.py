# a variable is the named location in memory that stores a value 
# a local variable is a variable that is defined within a function and is only aceesible within that function.
#it is created when a function is callled and is destroyed when the function returns.
# a global variable is a variable that is defined outside the function and is acssible from within  any 
# function with  your code.
# DEMO:
x = 10        #globle vairable
 
def my_function():
  y =5        #local variable
  print(y)
my_function()
print(x)
# print(y)<< # this will cause an error because y is a local variable and is not acessible outside the function.
 


# the global function changes the value of global variable form inside the function.
# DEMO:
x1 = 345

def hello_bhai():
  global x1
  x1= 98
  y1 = 122
  print(y1)
hello_bhai()
print(x1)
