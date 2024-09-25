# this file has all the classes (book, user, and author)
class Book:
# structures user inputs for book info neatly
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.available = True

    def __str__(self):
        status = "Available" if self.available == True else "Borrowed"
        return f"Title: {self.title} - Author: {self.author} - Genre: {self.genre}\nPublication Date: {publication_date} - Status: {status}"

class User:
# structures user info neatly, has borrow and return functionalities for the user
    def __init__(self, name, library_id)
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def __str__(self):
        return f"User Name: {self.name} - Library ID: {self.library_id}\n{self.name}'s Borrowed Books: {','.join(self.borrowed_books) or 'N/A'}"
    
    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book.title)
            print(f"'{book.title}' has been marked borrowed.")
        else:
            print(f"'{book.title}' is not available.")
    
    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book.title)
            print(f"'{book.title}' has been returned and marked available.")
        else:
            print(f"'{book.title}' was not marked as borrowed.")

class Author:
# structures user input for author
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio
    
    def __str__(self):
        return f"Author: {self.name} - Biography: {self.bio}"
        