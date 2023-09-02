# Tuples in python
# Tuples are orderd collection of data items.They store multiple items
# in a single variable.Tuple items are seperated by commas and 
# enclosed within round brackets().Tuples are unchangable meaning we can
# not alter them after creation.
 
# example#1
tup =(1,4,9,12)
print(type(tup),tup)
# tuples are immutable e.g.
# tup[0]= 56
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
# almost all process of tuple is same as list with minor difference

# slicing
# tuple= (34,6,1,8,9)
# tuple2= tuple[1:5]
# print(tuple2)



# OPERATION OF TUPLES IN PYTHON
# Manipulating Tuples
# tuples are immutable.Hence if you want to add,remove or change tuple
# it[em,then first you will have to cghange the tuple into list.then 
# perform operations on the list and again change it into a tuple
cities= ("lahore","london","multan","okara","tokyo","berlin")
temp= list(cities)
temp.append("sindh")          #add item
temp.pop(3)                   #remove item
temp[2]="gujrat"
cities= tuple(temp)
print(cities)

# Example#2
cities=("sialkot","sakhar","multan","peshawar","karachi","lahore")
name=("ali","usman","zain","umer","talha","hamza")
print(cities+name)

# tuple methods
# count()
# this method counts the number of times an element occurs in a tuple 
# e.g.
a=(1,3,5,7,9,1,3,5,8,9,1,3,1,2,1,6)
b= a.count(1)
print(b)
# index() gives us the location of element at first occurence
c=(2,4,6,8,0,12)
d= c.index(12)
print(d)

