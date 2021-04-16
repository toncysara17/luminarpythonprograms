class Employee:
    def emp_details(self,name,id,desig,sal):
        self.name=name
        self.id=id
        self.design=desig
        self.sal=sal
    def print(self):
        print(self.name)
        print(self.id)
        print(self.design)
        print(self.sal)
    def __str__(self):
        return



developer=list(filter(lambda emp:emp.desig=="developer",employees))
print(developer)
