#Question no2
class Person:
    def getname(self,name):
        self.name=name
        print(self.name)

class Address:
    def getadd(self,add):
        self.add=add
        print(self.add)


class Details(Person):
    def getdetails(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        print(self.first_name)
        print(self.last_name)
#Single Inheritance
# obj=Details()
# obj.getdetails("toncy","sara")
# obj.getname("toncy")


class Contact(Details):
    def getmobile(self,num):
        self.num=num
        print(self.num)
#Multiple inheritance
# obj1=Contact()
# obj1.getmobile(1234567891)
# obj1.getdetails("toncy","sara")
# obj1.getname("toncy")

class Profile(Person,Address):
    def getage(self,age):
        self.age=age
        print(self.age)
# Multilevel inheritance
obj2=Profile()
obj2.getage(20)
obj2.getadd("abcde")
obj2.getname("toncy")