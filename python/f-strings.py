# old  string formatting


letter = "Hey! My name is {}. I am from {}"
name = "Hamza"
country = "Pakistan"
print(letter.format(name, country))
# but if:
lttr="Hey! my name is{}.I am from{}"
nm= "Hamza"
cont= "Pakistan"
print(letter.format(cont,nm))
# this showss its draw back.old python developers  finished this by 
# indexing format e.g.
letter1="hey!my name is {1}.i am from {0}"
name1= "hamza"
count= "pakistan"
print(letter1.format(count,name1))


# modern string formatting:use f-string
essay="hey!my name is {}.i am {} years old.i am from {}"
nme="hamza"
age=18
place= "pakistan"
print(f"hey my name is {nme}.i am {age} years old.i am from{place}")
# example#2
price= 39.33333
txt= f"for only {price:.2f} dollars!!"
print(txt)
#example#3
print(f"{2*6}")        #it is string type
# if we want our input as it is in out put, we use {{}}e.g.
# example:
essay= "hey! my name is {}. i am a {}."
name = "hamza"
gend= "boy"
print(f"hey! my name is {{name}}.i am a {{gend}}")
