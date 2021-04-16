class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def printdet(self):
        print("name:",self.name)
        print("breed:",self.breed)
obj=Animal("dog","pug")
obj.printdet()

class Dog(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name,breed)
        self.age=age

    def printage(self):
        print("age:",self.age)
obj=Dog("dog","pug",2)
obj.printdet()
obj.printage()