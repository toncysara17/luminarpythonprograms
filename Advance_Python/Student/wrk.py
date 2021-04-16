class Work:
    def __init__(self,name,rollno,batch,mark):
        self.name=name
        self.rollno=rollno
        self.batch=batch
        self.mark=mark

    def printDetails(self):
        print(self.name)
        print(self.rollno)
        print(self.batch)
        print(self.mark)

f=open("work","r")
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    rollno=data[1]
    batch=data[2]
    mark=int(data[3])
    obj=Work(name,rollno,batch,mark)
    if(mark>190):
        obj.printDetails()
