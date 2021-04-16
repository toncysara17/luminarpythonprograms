class Book:
    def properties(self,name):
        self.name=name

    def details(self):
        print(self.name)
class Child(Book):
    def details(self):
        print("book details")

c=Child()
c.details()