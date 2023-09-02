# Docstrings in python 
# docstrings are the string literals that apear right after the
#  definition of a function,method,class,module.
# example
def square(n):
    '''takes in a number n,returns the square of n'''
    print(n**2)
square (5) 
# docstrings are not ignored as compared to strings e.g.
print(square.__doc__)   #doc string should be placed right above the function body



# recursion in python
# recursion is the process of defining somethingin terms of itself


# factorial (7)= 7*6*5*4*3*2*1
# factorial (6)= 6*5*4*3*2*1
# factorial (5)= 5*4*3*2*1
# factorial (4)= 4*3*2*1
# factorial (0)= 1
# factorial(n)= n * factorial(n-1) 
def factorial(n):
    if(n==0 or n==1):
        return 1 
    else:
        return n* factorial(n-1)
print(factorial(6))
