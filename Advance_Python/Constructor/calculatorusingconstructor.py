class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def mult(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2

    def power(self):
        return self.num1**self.num2

    def modulus(self):
        return self.num1%self.num2

    def floor(self):
        return self.num1//self.num2
obj=Calculator(10,20)
print(obj.add())
print(obj.sub())
print(obj.mult())
print(obj.div())
print(obj.power())
print(obj.modulus())
print(obj.floor())