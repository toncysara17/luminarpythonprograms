#Oops
class Person:
    def persondetails(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name :",self.name)
        print("age :",self.age)
obj=Person()
obj.persondetails("tom",12)
obj.printvalue()