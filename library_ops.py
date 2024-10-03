# this file has all functions for book, user and author operation menues
# it has been updated to include database interaction, the classes were kept the same
import mysql.connector
from connect_db import connect_database
from library_classes import Book, User, Author

books = []
users = []
authors = []
conn = connect_database()
cursor = conn.cursor()

# these functions are for the book operations menu (add, borrow, return, search, and display)
def add_book():
    title = input("Enter book title: ").title()
    author = input("Enter author's name: ").title()
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ").title()
    publication_date = input("Enter publication date: ")
    # removed former book class integration, now finding author in database and adding author if not in database
    cursor.execute("SELECT id FROM authors WHERE name = %s", (author,))
    result = cursor.fetchone()
    if result:
        author_id = result[0]
    else:
        add_author()
    # adding book to database
    cursor.execute("INSERT INTO books (title, author_id, publication_date) VALUES (%s, %s, %s, %s)")
    print(f"'{title}' has been added to the library.")

def borrow_book():
    title = input("Enter book title to borrow: ").title()
    for book in books:
        if book.title == title:
            library_id = input("Enter user's library ID: ")
            user = find_user(library_id)
            if user:
                user.borrow_book(book)
                return
        else:
            print(f"'{title}' was not found in the library, please try a different book.")

def return_book():
    title = input("Enter book title to return: ").title()
    for book in books:
        if book.title == title:
            library_id = input("Enter user's library ID: ")
            user = find_user(library_id)
            if user:
                user.return_book(book)
            return
        else:
            print(f'{title} was not found in the system. Please add it')

def search_book():
    title = input("Enter book title to search: ").title()
    print("~ Search Result ~")
    for book in books:
        if book.title == title:
            print(book)
        else:
            print(f"'{title}' was not found in the library, try a different book.")

def display_books():
    if books:
        for book in books:
            print(book)
    else:
        print("Library list empty. Please add books to the system")

# these functions are for user operations menu (add, view and display users)
def find_user(library_id):
        for user in users:
            if user.library_id == library_id:
                return user
        return None

def add_user():
    name = input("Enter user name: ").title()
    library_id = input("Enter Library ID: ")
    if library_id not in users:
        user = User(name, library_id)
        users.append(user)
        print(f"'{name}' has been added and is ready to borrow books")
    else:
        print(f"Library ID {library_id} already taken, please assign a different ID.")

def view_user():
    library_id = input("Enter Library ID for user search: ")
    user = find_user(library_id)
    if user:
        print(user)
    else:
        print(f"Library ID '{library_id}' not found, please try again.")

def display_users():
    if users:
        for user in users:
            print(user)
    else:
        print("No users registered. Please add users")

# these are the author operations menu functions (add, view and display authors) 
def add_author():
    name = input("Enter author name: ").title()
    bio = input("Enter author biography (brief description): ")
    # removed author class integration and added database integration for the authors table
    cursor.execute("INSERT INTO authors (name, biography) VALUES (%s, %s)", (name, bio))
    conn.commit()
    author_id = cursor.lastrowid
    print(f"'{name}' has been added to the authors list")

def view_author():
    name = input("Enter author name to view: ").title()
    print("~ Search Result ~")
    for author in authors:
        if author.name == name:
            print(author)
            return
    print(f"'{name}' was not found in the authors list. Please add the author")

def display_authors():
    if authors:
        for author in authors:
            print(author)
    else:
        print("Authors list empty, please add authors")