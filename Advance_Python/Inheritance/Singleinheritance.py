#inheritance

#single inheritance


class Parent:                   #parent class or super class
    parent_name="Arun"              #instance variable
    def m1(self,age):
        self.age=age
        print("my name is",Parent.parent_name)
        print(self.age)

class child(Parent):                #derived class or child class
    def m2(self,cage):
        self.cage=cage
        print("parent name is",Parent.parent_name)
        print(self.age)
        print(self.cage)
c=child()
c.m1(23)
c.m2(12)