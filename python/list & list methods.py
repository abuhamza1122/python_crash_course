# introduction to lists in python
# lists are ordered collection of data types and store multiple items
# in a single variable

# example 1
marks=[23,45,67,89,]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
# negative indexing 
print(marks[-3])
# for negative indexing we use the total lenght of the list and subtract
# it to the given number,remember that indexing starts from 0 but 
# lenght starts from 1
if 45 in marks:
    print("yes")
else:
    print("no")
# slicing
# example#1
group= ["hamza","talha",2,8,3,5]
print(group)
print(group[1:5])
# list comprehension
lst=[i for i in range(4)]
print(lst)

lst=[i*i for i in range(10) if i%2==0]
print(lst)
# list methods in python
l= [1,2,4,6,89,11]

# we will use append method to add the element at the end of the list
l.append(9)
print(l)
# sort function arranges the list in assending order
l.sort()
print(l)
# if we want decending order we will apply
l.sort(reverse=True)
# reverse method reverses the original or given list
l2= [2,7,90,12,45,67]
l2.reverse()
print(l2)
# index method returns the index of first occurence
l3= [23,12,1,1,1,1,1,87,9,67]
print(l3.index(9))
# count () counts the number of times a number reapeats
print(l3.count(1))
# insert() inserts an item at the given index.user has to specify index
# and the item to be inserted within the insert method
l3.insert(2,6)
print(l3)
# extend()
# this method adds an entire list or any other collection data type(set,
# tuple,dict) to existing data list
a= [34,41,69,54]
m= [98,19,73,48,53]
a.extend(m)
print(a)
# in simple method, we can easily imagne a new variable which is equal
# the sum of two variable e.g
k= a+m
print(k)
