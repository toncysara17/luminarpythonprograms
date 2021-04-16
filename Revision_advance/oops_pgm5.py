#using Oops
class Employee:
    def emp_details(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def printvalue(self):
        print("name:",self.name)
        print("id:",self.id)
        print("salary:",self.salary)

obj=Employee()
obj.emp_details("tom",10,10000)
obj.printvalue()