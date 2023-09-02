# "is" and "==" are both comparison operatiors with a minimum difference.
# "is" compares the exact location of object in memory and "==" compares the value 
a= 4
b="4"
print(a is b)  #location of object in memory (compares the identity of object in history)
print(a==b)    #value (compares if the value of two variables is same or not)
# the output will be false because neither the value is same nor the location of object is same
#for constants,both value and location of objects can be same and in this case,the output will be true for both
# for lists, the values can be same but the location will be not the same in memory
# DEMO 1: for lists
a1= [1,2,3,4]
b1= [1,2,3,4]
print(a1 is b1) #false because there are different locations of these variables in memory
print(a1==b1)   #true because both are same in value

# DEMO 2:
a2 =785
b2 =785
print(a2 is b2)    #true because if constants are equal,they will be sotre in same place in memory
print(a2 == b2)    #true because these constants are equal to each other
x = None
y = None
print(x is y)    #we can also put the value of variables e.g. 'x is None' etc
print(x==y)

 
