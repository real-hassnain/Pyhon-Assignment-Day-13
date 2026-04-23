#TASK 5

class Book:
    def __init__(self, title, author, pages, is_available):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_available = is_available
    def summary(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)
        
        if self.pages > 300:
            print("Long Read")
        else:
            print("Short Read")
        
        if self.is_available:
            print("is Available")
        else:
            print("is not Available")
        print()



b1 = Book("Python Basics", "John Smith", 250, True)
b2 = Book("Data Structures", "Jane Doe", 420, False)


b1.summary()
b2.summary()

