# break statement in pyhton 
for i in range(12):
    print("5 X",i+1,"=",5*(i+1))
    if(i==10):
        break
print("skip the loop")


# continue statement in python
i = 0
for i in range (12):
    if(i==10):
    #   print("skip the iteration")
    #   continue 
        pass
    print("5 X",i+1,"=",5*(i+1))