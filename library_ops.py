from library_classes import Book, User, Author

books = []
users = []
authors = []

# these functions are for the book operations menu (add, borrow, return, search, and display)
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author's name: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date: ")
    book = Book(title, author, genre, publication_date)  # passes through book info to the Book class in library_classes.py
    books.append(book) # adds book to the list of books
    print(f"'{title}' has been added to the library.")

def borrow_book()