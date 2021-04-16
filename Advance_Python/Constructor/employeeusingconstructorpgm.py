class Employee:
    company_name="Luminar Technolab"
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def printvalu(self):
        print(self.name)
        print(self.id)
        print(Employee.company_name)
obj=Employee("abc",111)
obj.printvalu()