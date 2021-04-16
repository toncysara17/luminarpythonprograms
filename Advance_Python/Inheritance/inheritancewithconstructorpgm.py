#person pgm using inheritance with constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printVal(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)                      #call by super class constructor
        self.rollno=rollno
        self.mark=mark
        self.name=name
        self.age=age
    def printValue(self):
        print("rollno",self.rollno)
        print("mark",self.mark)
obj=Student(1,30,"anu",23)
obj.printVal()
obj.printValue()