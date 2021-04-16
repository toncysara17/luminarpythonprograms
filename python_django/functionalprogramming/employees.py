class Employee:
    def __init__(self,eid,ename,design,sal):
        self.eid=eid
        self.ename=ename
        self.design=design
        self.sal=sal

    def print(self):
        print(self.ename)
f=open("emp1")
employees=[]
for line in f:
    data=line.rstrip("\n").split(",")
    eid,ename,design,sal=line.rstrip("\n").split(",")

    def __str__(self):
        return  self.design+self.ename
emp=Employee(1002,"anu","developer",24000)
emp1=Employee(1003,"tom","developer",20000)
employees = []
employees.append(emp)
employees.append(emp1)
devop=list(filter(lambda emp:emp.design=="developer",employees))
for dev in devop:
    print(dev)


#e1=Employee(eid,ename,design,sal)

#employees.append(e1)


for emp in employees:
    print(emp.design)
sal=list(map(lambda emp:emp.sal,employees))
higsal=max(sal)
print(higsal)
# developers=list(filter(lambda emp:emp.design=="developer",employees))
# print(developers)


