#constructor
#calculator pgm
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def div(self):
        print(self.num1/self.num2)
obj=Calculator(30,20)
obj.add()
obj.sub()
obj.div()
