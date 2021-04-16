#person program using multilevel or hierarchial inheritance
class Person:
    def m1(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        print("first_name is",self.first_name)
        print("last_name is",self.last_name)

class Person1(Person):
    def m2(self,age):
        self.age=age
        print("age is",self.age)

class Person2(Person1):
    def m3(self,middle_name):
        self.middle_name=middle_name
        print("middle_name is",middle_name)

obj=Person2()
obj.m3("ghi")
obj.m2(20)
obj.m1("abc","def")

