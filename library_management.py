class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []
        self.noOfBooks = len(self.books)
    
    def addBook(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)
        print(f"Book '{book}' added successfully.")

    def showBooks(self):
        print(f"Your books: {self.books}")
        
    def checkNoOfBooks(self):
        return self.noOfBooks == len(self.books)

l1 = Library(["Hey", "hi", "hello"])

l1.addBook("Ashwini")

l1.showBooks()

is_consistent = l1.checkNoOfBooks()
print(f"Is book count consistent? {is_consistent}")

