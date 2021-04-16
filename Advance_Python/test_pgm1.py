class Vehicle:
    def m1(self,name):
        self.name=name
        print("name",self.name)
class Bus(Vehicle):
    def m2(self,price):
        self.price=price
        print("price",self.price)
obj=Bus()
obj.m1("tom")
obj.m2(50000)
