#multilevel inheritance or hierarchial inheritance
class Parent:
    def m1(self):
        print("inside parent")

class Child(Parent):
    def m2(self):
        print("inside child class")

class  Subchild(Child):
    def m3(self):
        print("inside subchild")

obj=Subchild()
obj.m3()
obj.m2()
obj.m1()
obj=Child()
obj.m2()
obj.m1()