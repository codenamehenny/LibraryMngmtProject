# This is the Book Operations file containing the Book Class

class Book:
    def __init__(self, title, author, borrowed = False):
        self.title = title
        self.author = author
        self.borrowed = borrowed

class Library:
    def __init__(self): # empty library list
        self.books = []
# adds a book to the library list
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"'{title}' by '{author}' added to the library.")
# changes book's borrow status to True     
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.borrowed:
                    book.borrowed = True                    
# return a book function updates book borrowed status back to False
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrowed:
                    book.borrowed = False
                    print(f"'{book.title}' has been returned.")
                else:
                    print(f"'{book.title}' was not marked as borrowed.")
            else:
                print(f"'{book.title}' was not found in the library, please add it first.")
# searches for a book
    def search_book(self, title):
        if not books:
            print("Library list empty. Please add some books")
        for book in self.books:
            if title.title() in book.title.title():
                if book.borrowed:
                    status = "Borrowed"
                elif not book.borrowed:
                    status = "Ready to borrow"
                print(f"Search Result:\nBook:{book.title} -- Author:{book.author} -- Status:{status}")
            else:
                print(f"'{book.title}' not found in the library.")
# this displays all the books available 
    def display_books(self):
        if not self.books:
            print("There are no books in the library.")
        else:
            for book in self.books:
                if book.borrowed:
                    status = "Borrowed"
                elif not book.borrowed:
                    status = "Ready to borrow"
                print(f"~ Book:{book.title} -- Author:{book.author} -- Status:{status}")

def book_ops_menu():
    library = Library()
    while True:
        try:
            print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book")
            print("4. Search for a book\n5. Display all books\n6. Return to Main Menu")
            option = int(input("Enter option number: "))
            if option == 1:
                title = input("Enter book title: ")
                author = input("Enter book auhtor: ")
                library.add_book(title, author)
            elif option == 2:
                title = input("Enter book title to borrow: ")
                library.borrow_book(title)
            elif option == 3:
                title = input("Enter book title to return: ")
                library.return_book(title)
            elif option == 4:
                title = input("Enter book title to search: ")
                library.search_book(title)
            elif option == 5:
                library.display_books()
            elif option == 6:
                print("Returning to main menu...")
                break
            else:
                print("Please enter a number between 1-6")
        except ValueError:
            print("Please enter a valid number")
        except Exception as e:
            print(f"Error message: '{e}', please try again.")