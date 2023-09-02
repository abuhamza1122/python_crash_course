# ITERATION IN LOOPS
# example#1
name= 'Hamza'
for i in name:
    print(i)
# Example#2
place ='KhyberPakhtunKhua'
for i in name:
    print(i,end="~")
# We can iterate our strings with the help of loops as well as lists
# example for list:(We will use "x")
colour= ["red","green","blue","brown"]
for x in colour:
    print(x)
# we can also use the initial name e.g colour 
for colour in colour:
    print(colour)
# we can put if statement also in loop e.g.
    for i in colour:
        print(i)
        if(i=="b"):
            print("noice")
# Range ()
# it is used to collect sequence of numbers starting from zero and ending with n-1
# Example#1
for k in range(6):
    print(k)
# Example#2(we can make changes in print statement)
for k in range(7):
    print(k-1)
# we can also give the input from where it start we want
for k in range(1,10):
    print(k)
# While loop:
# Example#1
for i in range(6):
    print(i)
i = 0
while(i<=6):
    print(i)
    i = i +1
# Example#2
i= int(input("enter your number:"))
while(i <= 40):
  i= int(input("enter your number:"))
  print(i)
print("Done with the loop")# this is for confirmation if the number is big
# decreamenting loop example:
num= 5
while(num>0):
    print(num)
    num= num-1
