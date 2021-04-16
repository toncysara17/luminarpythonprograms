class Person:       #create class
    def setval(self,name,age):          #method using funct
        self.name=name                  #define using self
        self.age=age
    def printvalue(self):
        print("name:",self.name)            #call
        print("age:",self.age)
obj=Person()                                #obj create by reference
obj.setval("ram",23)                        #obj call by reference
obj.printvalue()