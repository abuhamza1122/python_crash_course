# SETS IN PYTHON 
# Sets are well defind collection of objects. the values do not repeat 
# in sets,no garranty of order maintanence,identified by curly {}
s = {2,4,2,6}
print(s)

# example2
info = {9,"Hamza",None,True,9.3}
print(info)
for value in info:
    print(value)

n= set()   #  this is the method to writee an empty set other wise 
# it will change its class to dict 
print(type(n))

# SET METHODS IN PYTHON
# UNION(MERGES TWO SETS WITH SEQUENCE,SMALLER TO LARGER IN NUMBERS)
s1 = {1,3,5,7}
s2 = {2,4,5,8}
print(s1.union(s2))
# UPDATE FUNCTION:
s1.update(s2)
print(s1,s2)
# INTERSECTION
city1 = {"tokyo","madrid","lahore"}
city2 = {"karachi","islamabad","lahore","tokyo"}
print(city1.intersection(city2))
city1.intersection_update(city2)
print(city1)

# SYMMETRIC DIFFERENCE [(A U B)- (A INTERSECTION B)] doesnot follow order and contains element which are not common
cities1 = {"berlin","moscow","tokyo","lahore"}
cities2= {"moscow","lahore","delhi","kashmir","ladakh"}
cities3=cities1.symmetric_difference(cities2)
print(cities3)
# DIFFERENCE(takes only those elements which are present in 1st set only) &DIFFERENCE UPDATE
name1= {"hamza","ahmad","fayyaz","riaz"}
name2 = {"alia","ayesha","bisma","sadia","talha"}
name3= name1.difference(name2)
print(name3)
# ISDISJOINT():If two sets have nothing in common they are called disjoint(it gives ans in boolean)
a1 ={1,2,4,3,6,8}
b1= {3,6,8}
c1= a1.isdisjoint(b1)        #false
print(c1)
# ISSUPERSET: set B is said to be superset of set A if all the elements of B are present in set A
c2= a1.issuperset(b1)
print(c2)                    #true
# ISSUBSET : set A is set to be subset of set B if all the elements of set A are present in set B
c3= a1.issubset(b1)
print(c3)                    #false


# ADD() :adds elements in set ;does not follow order of set
H= {"horse","hamza","huma","haima"}
H.add("hello")            #"hello" added in set
print(H)
# REMOVE (): REMOVES ELEMENTS PRESENT IN SET; if the given element is not present in set,error occurs
H.remove("horse")
print(H)                  #horse removed

# DISCARD(): It is same as remove function but never throws error if element is not present in set
H1= {"rida","shida"}
H1.discard("bilal")
print(H1)             #did not threw error

# POP(): removes a random element from the set 
H1.pop()          #a random element will be removed
# DElete METHOD: deletes the entire set along its entries e.g 
# del H1
# print(H1)

# CLEAR(): deletes all the entries but not the set 
H1.clear()
print(H1)
   



#    CHECK IF ITEM EXIST:
INFO= {"one","two","three","four"}
if("two" in INFO):
    print("yessssss")
else:
    print("jaldi wahan se hatto")        #yessssss is printed



