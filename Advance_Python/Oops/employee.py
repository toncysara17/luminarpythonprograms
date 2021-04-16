class Employee:
    def setval(self,ename,eid,esal):
        self.ename=ename
        self.eid=eid
        self.esal=esal
    def printval(self):
        print("ename:",self.ename)
        print("eid:",self.eid)
        print("esal:",self.esal)
obj=Employee()
obj.setval("tom",1001,100000)
obj.printval()