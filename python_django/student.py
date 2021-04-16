class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.couse=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(10,"tona","python",2000)
s2=Student(11,"tona","java",2001)
s3=Student(12,"tona","php",2002)
studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)
studenttotal=list(map(lambda std:std.total,studentlist))
print(max((studenttotal)))
