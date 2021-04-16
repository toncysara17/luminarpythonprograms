#Constructor
#it is used to initaialize object
#its automatically  invoke when creating object

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print(self.name)
        print(self.age)
obj=Person("abc",11)
obj.printvalue()