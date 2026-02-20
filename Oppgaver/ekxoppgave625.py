class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    def showInfo(self):
        print(self.title, self.author, self.borrowed)

class Borrower():
    Borrowers = []
    def __init__(self):
        Borrower.Borrowers.append(self)
        self.ID = len(Borrower.Borrowers)
        self.books = []
    def borrowBook(self, book):
        if book.borrowed == False:
            self.books.append(book)
            book.borrowed = True
    def returnBook(self, book):
        if book in self.books:
            self.books.remove(book)
            book.borrowed = False

AoW = Book("Art of War","Sun Tzu")
GO = Book("1984","George Orwell")
HP = Book("Harry Potter","J. K. Rowling")
B = Book("Bibelen","Gud")

JensStoltenberg = Borrower()

JensStoltenberg.borrowBook(AoW)
print(JensStoltenberg.books)

        

