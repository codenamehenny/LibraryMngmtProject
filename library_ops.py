# this file runs operations for book, user and author menues

from library_classes import Book, User, Author
from connect_db import connect_database

# these functions are for the book operations menu (add, borrow, return, search, and display)
def add_book():
    try:
        title = input("Enter book title: ").title()
        author_name = input("Enter author's name: ").title()
        isbn = input("Enter ISBN: ")
        publication_date = input("Enter publication date: ")
        # passing book details to Book class
        book = Book(title, author, isbn, publication_date)  # passes through book info to the Book class in library_classes.py
        books.save() # saves book details to database
        except Exception as e:
            print(f"Error message: {e}. Book details failed to save, please try again.")

def borrow_book():
    try:
        title = input("Enter book title to borrow: ").title()
        library_id = input("Enter library ID: ")
        # getting book and user
        book = Book.search_book_title(title)
        if book:
            book.mark_as_borrowed(library_id)
            print(f"{book.title} is now marked as borrowed.")
        else:
            print(f"{title} not found in library. Please add it to the library before checking out")
    except Exception as e:
        print(f"Error message: {e}. The book failed to be checked out, please try again.")

def return_book():
    try:
        title = input("Enter book title to return: ").title()
        library_id  = input("Enter library ID: ")
        # getting book from database
        book = Book.search_book_title(title)
        if not book:
            print(f"{title} was not registered in the database. Please register the book and check it in.")
            return
        if book.availability:
            print(f"{book.title} is already marked available. No further action needed.")
            return
        book.return_book(library_id)
        print(f"{book.title} was been successfully return and marked as available.")
    except Exception as e:
        print(f"Error Message: {e}. The book failed to be marked as returned, please try again")

def search_book():
    try:
        title = input("Enter book title to search: ").title()
        book = Book.search_book_title(title)
        print("~ Search Result ~")
        if book:
            status = 'Available' if book.availability else 'Borrowed'
            print(f"Title: {book.title}, Author: {book.author.name}, ISBN: {book.isbn}, 
                Publication Date: {book.publication_date}, Availability: {status}")
        else:
            print(f"{title} was not found in the library.")
    except Exception as e:
        print(f"Error Message: {e}. The search could not be completed, please try again")
        
def display_books():
    try:
        books = Book.get_all_books()
        if books:
            for book in books:
                status = 'Available' if book.availability else 'Borrowed'
                print(f"Title: {book.title}, Author: {book.author.name}, ISBN: {book.isbn}, 
                    Publication Date: {book.publication_date}, Availability: {status}")
        else:
            print("No books are registered in the library")
    except Exception as e:
        print(f"Error Message: {e}. Request to display books failed, please try again")

# these functions are for user operations menu (add, view and display users)
def find_user(library_id):
    try:
        library_id = input("Enter the user's library ID: ")
        user = User.search_by_library_id(library_id)
        if user:
            print(f"User found:\nName: {user.name} -- Library ID: {user.library_id}")
        else:
            print(f"Library ID {library_id} was not found")
    except Exception as e:
        print(f"Error Message: {e}. Failed to get user details, please try again")

def add_user():
    try:
        name = input("Enter user name: ").title()
        library_id = input("Enter Library ID: ")
        # checking for existing library id's to ensure no duplicates
        existing_user = User.search_by_library_id(library_id)
        if existing_user:
            print(f"Library ID {library_id} already registered. Please use a different ID")
        else:
            user = User(name = name, library_id = library_id)
            user.save()
            print(f"'{name}' has been added and is ready to borrow books")
    except Exception as e:
        print(f"Error Message: {e}. User failed to save, please try again")

def display_users():
    try:
        users = User.get_all_users()
        if users:
            print("Here's the full list of registered users:")
            for user in users:
                print(f"Name: {user.name} -- Library ID: {user.library_id}")
        else:
            print("No users registered. Please add users to the library")
    except Exception as e:
        print(f"Error Message: {e}. Users failed to load, please try again")


# these are the author operations menu functions (add, view and display authors) 
def add_author():
    try:
        name = input("Enter the author's name: ").title()
        biography = input("Enter author biography: ")
        author = Author(name = name, biography = biography)
        author.save()
        print(f"{name} added successfully")
    except Exception as e:
        print(f"Error Message: {e}. Failed to add author, please try again")


def view_author():
    try:
        name = input("Enter the author's name: ").title()
        author = Author.search_author_name(name)
        if author:
            print(f"Author found:\nName: {author.name} -- Biography: {author.biography}")
        else:
            print("Author not found")
    except Exception as e:
        print(f"Error Message: {e}. Failed to load authors, please try again")

def display_authors():
    try:
        authors = Author.get_all_authors()
        if authors:
            print("Here are the registered authors in the library")
            for author in authors:
                print(f"Name: {author.name} -- Biography: {author.biography}")
        else:
            print("No authors registered. Please add authors")
    except Exception as e:
        print(f"Error Message: {e}. Failed to display all authors, please try again")