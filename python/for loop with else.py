# FOR LOOP WITH ELSE IN PYTHON
# DEMO:
for i in range(5):
    print(i)
else:
    print("bhai bhai bhai")

# DEMO 2 :
for k in range(7):
    print(k)
    if k ==4:
        break
else:
    print("hello jawn")         #else will not be printed as breeak statement breaks the program 
# if else is printed,it means that the program did not break,it was finished up to its last entry
# EXAMPLE:1
for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("out of loop")
