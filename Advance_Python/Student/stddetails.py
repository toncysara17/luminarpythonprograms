class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printDetails(self):
        print(self.name)
        print(self.age)
    def __str__(self):
        return self.name
f=open("Std","r")
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    obj=Student(name,age)
    obj.printDetails()
