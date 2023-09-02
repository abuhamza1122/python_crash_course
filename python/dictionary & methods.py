# DICTIONARIES IN PYTHON 
# dictionaries are ordered collection of data items.they store multiple
# items in a single variable.dictionary items are key value pairs
# that are seperated by commas and enclosed within {} 
# EXAMPLE#1
dict = {
    "Hamza" : "Human Being",
    "Spoon"  : "object"
}
print(dict["Spoon"])
# EXAMPLE#2
info = {"name" : "hamza", "age" : 18 , "gender" : "male"}
print(info["name"])            #it will give an error if the entry is not present in your function
print(info.get('name'))        # it will give none if the entry is not present in your function
   


sett = {'name' : 'Hamza', 'name2' : 'Talha' , 'name3' : 'Fayyaz'}
print(sett)
print(sett.keys())

for key in sett.keys():     #"key" and "keys" are two different function
  print(sett[key])
# with key function we can have keys and  with value function we get values

# DICTIONARY METHODS IN PYTHON:
# update()
ep1 ={"q":76 ,"w":94 ,"e": 59}
ep2 ={"r":99,"t":82,"y":41}
ep1.update(ep2)
print(ep1)
# clear(): clears all the entries of dictionary e.g
# ep1.clear()
# print(ep1)


# pop(): removes the  element from dictionary which we want (removes key value pair)
z= {1:2,3:4,5:6}
z.pop(5)
print(z)     # removed the pair
# popitem(): removes the last key value pair
z1={89:98,12:54,87:18} 
z1.popitem()
print(z1)

# DEL ():Deletes the entire ditionary 
x= {23:63,76:123,55:39}
# del x                 
# print(x)             if we print,error occurs
# we can delete any entry with the help of del()
del x[23]
print(x)







