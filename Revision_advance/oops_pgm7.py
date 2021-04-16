#using oops
class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.sum=num1+num2
    def printval(self):
        print("num1:",self.num1)
        print("num2:",self.num2)
        print("res:",self.sum)
obj=Addition()
obj.add(10,20)
obj.printval()

