# Importing in python is the process of loading code from a python module into the current script.as well as 
# any additional module that the imported module may depend on.
# DEMO:
import math
result=math.sqrt(9)
print(result)           #result= 3.0
# DEMO 2:
from math import sqrt,pi
result1= sqrt(4)*pi 
print(result1)
# IMPORTING EVERY THING:it is also possible to import all functions and variables from a module using a * 
# wildcard(from math import *) it is not recommended because it is very confusing
# example
from math import *
result2= sqrt(16)*pi
print(result2)

# THE as KEYWORD:mkes function in short form by taking any word that exchanes the function e.g.
import math as m
result3=m.sqrt(25)*pi
print(result3)



# DIR FUNCTION:dir([object]) -> list of strings
# If called without an argument, return the names in the current scope. Else, return an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it. If the object supplies a method named __dir__, it will be used; otherwise the default dir() logic is used and returns:
#   for a module object: the module's attributes.
#   for a class object: its attributes, and recursively the attributes
#     of its bases.
#   for any other object: its attributes, its class's attributes, and
#     recursively the attributes of its class's base classes.
import math
print(dir(math))








