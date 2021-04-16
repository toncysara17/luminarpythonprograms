#using static variable

class Employee:
    company_name="Luminar Technolab"
    def emp_details(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal
    def printval(self):
        print("name:",self.name)
        print("id:",self.id)
        print("sal:",self.sal)
        print(Employee.company_name)
obj=Employee()
obj.emp_details("tom",10,10000)
obj.printval()