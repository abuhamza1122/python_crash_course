# # DEMO:
# def cube(x):
#     return x*x*x
# l= [1,4,9,4,3,2]
# l1= []
# for i in l:
#     l1.append(cube(i))
# print(l1)
# # so we can have cubes of the elements of list by this method but this is very time consuming
# # so we will use "MAP()"
# def cube(a):
#     return a*a*a
# lst1 = [7,9,2,5,7,1]
# lst2 = list(map(cube,lst1))
# print(lst2)
# # FILTER(): filters the elements according to condition
# def filter_function(f):
#     return f>6
# list0= [8,6,6,2,66,90]
# list00= list(filter(filter_function,list0))
# print(list00)
# # keep it in mind,you have to give type of function in which you wanna convert it.e.g.list 


# # in lambda function 
# d = [2,5,78,3,6,1]
# d1= list(map(lambda x:x*x*x,d))
# print(d1)

# reduce() it is supposed to import,otherwise it will be useless
# DEMO: 
from functools import reduce

#List of numbers
num=[1,2,3,4,5,6]

# calculate the sum of the numbers using the reduce function 
sum = reduce( lambda x,y : x+y,num) 
# print the sum 
print (sum)














