#student pgm using single inheritance
class Student:
    Student_name="anu"
    def stddetails(self,rollno,batch):
        self.rollno=rollno
        self.batch=batch
        print("my name is",Student.Student_name)
        print(self.rollno)
        print(self.batch)

class Student1(Student):
    def std1(self):
        print("student name is",Student.Student_name)
        print(self.rollno)
std=Student1()
std.stddetails(15,"cse")
std.std1()