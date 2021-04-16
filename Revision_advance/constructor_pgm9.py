#constructor
class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def printval(self):
        print("first_name:",self.first_name)
        print("last_name:",self.last_name)
obj=Person("toncy","sara")
obj.printval()