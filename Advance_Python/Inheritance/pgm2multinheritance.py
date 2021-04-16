#create two parent classes father,mother and get their corresponding details
# and inherit this classes to a child class name kid
#kids information and print all details in child class
#using multiple inheritance

class Father:
    def m1(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
        print("father name is",self.name)
        print("age is",self.age)
        print("father occupation is an",self.occupation)

class Mother:
    def m2(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
        print("mother name is",self.name)
        print("age is",self.age)
        print("mother occupation is an",self.occupation)

class Kid(Father,Mother):
    def m3(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("name is",self .name)
        print("age is",self.age)
        print("gender is",self.gender)

obj=Kid()
obj.m3("tom",2,"Female")
obj.m2("anu",20,"engg")
obj.m1("manu",25,"doctor")