class Book:
    def book_details(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printval(self):
        print("library name:",self.library_name)
        print("bookname:",self.book_name)
        print("author:",self.author)
        print("pages:", self.pages)
obj=Book()
obj.book_details("National library","wings of fire","APJ.Abdul Kalam","250")
obj.printval()
