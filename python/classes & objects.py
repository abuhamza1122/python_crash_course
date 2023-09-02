# A class is a blueprint or a template for creating objects, providing initial values for state (member
# variables or attributes), and implementations of behavior (member functions or methods). The user-defined
#  objects are created using the class keyword.
# DEMO:
class Person:
    Name = "Hamza"
    Occupation = "King"
    NetWorth= 100000
    Age = 18
    def info(self):
        print( f"hello! my name is {self.Name}.I am a {self.Occupation}") 
a = Person()

print(a.Name)
a.Name = "Fayyaz"       # for changing in name
print(a.Name)     
print(a.Occupation)   
a.Occupation = "Software Developer"  #we can do anything by doing this step
print(a.Occupation)
a.info()
# SELF:The self parameter is a reference to the current instance of the class, and is used to access variables
#  that belongs to the class.
# It must be provided as the extra parameter inside the method definition.
# self ka matlab wo object jis pe method call kia ja raha hai 






































