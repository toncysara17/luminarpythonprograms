class Employee:
    company_name="Luminar Technolab"
    def empdetais(self,name,id):
        self.name=name
        self.id=id
    def printval(self):
        print(self.name)
        print(self.id)
        print(Employee.company_name)
obj=Employee()
obj.empdetais("abc",11)
obj.printval()