#addition of two numbers
class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.sum=num1+num2
    def printsum(self):
        print("num1 is",self.num1)
        print("num2 is",self.num2)
        print("sum is",self.sum)
obj=Addition()
obj.add(10,20)
obj.printsum()