#identify id using string
class Employee:
    company_name="Luminar Technolab"
    def empdetails(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary

    def printVal(self):
        print("company name is",Employee.company_name)
        print("name is",self.name)
        print("age is",self.age)
        print("id ",self.id)
        print("salary",self.salary)
    def __str__(self):
        return str(self.id)
emp=Employee()
emp.empdetails("anu",20,2,1000)
print(emp)