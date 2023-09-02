# A constructor is a unique function that gets called automatically when an object is created of a class.
# The main purpose of a constructor is to initialize or assign values to the data members of that class. It
#  cannot return any value other than None.
class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
# DEMO:
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()