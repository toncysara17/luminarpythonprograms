#Two strings method
class College:
    collegename="LT"

    def __int__(self,name,rollno):
        self.rollno=rollno
        self.name=name

    def printDetails(self):
        print("college name is",College.collegename)
        print("name of student is",self.name)
        print("rollno",self.rollno)
    def __str__(self):
        return self.name+str(self.rollno)
obj=College("anu",4)
print(obj)