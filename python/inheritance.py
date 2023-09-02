class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetail(self):
        print( f"The name of Employee: {self.name} and his id is {self.id}")

e2= Employee ("Talha",421)
e2.showDetail()
e3 = Employee ("Abdullah",422)
e3.showDetail()
e4 = Employee ("Fayyaz",423)
e4.showDetail()
e5 = Employee ("Ijaz",424)
e5.showDetail()