class Employee:
    companu_name="Luminar Technolab"
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal
    def printval(self):
        print("name:",self.name)
        print("id:",self.id)
        print("sal:",self.sal)
        print(Employee.companu_name)
obj=Employee("tona",12,10000)
obj.printval()