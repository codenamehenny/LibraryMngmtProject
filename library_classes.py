# this file has all the classes (book, user, and author)
# the classes have been updated with database integration
from connect_db import connect_database

class Book:
# structures user inputs for book info neatly
    def __init__(self, title, author, isbn, publication_date, availability = True, id = None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isgn
        self.publication_date = publication_date
        self.availability = availability

    def save_book(self):
        conn = connect_database()
        cursor = conn.cursor()
        # checking to see if author exists and saving the author first if it doesn't
        if not self.author.id:
            self.author.save()
        if self.id:
            cursor.execute("""
                UPDATE books SET title = %s, author_id = %s, isbn = %s, 
                publication_date = %s, availability = %s WHERE id = %s
                """, (self.title, self.author.id, self.isbn, self.publication_date, self.availability))
        else:
            cursor.execute("""
                INSERT INTO books (title, author_id, isbn, publication_date, availability)
                VALUES (%s, %s, %s, %s, %s)""",
                (self.title, self.author_id, self.isbn, self.publication_date, self.availability))
                self.id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
    
    def search_book_title(self, title):
        conn = connect_database()
        cursor = conn.cursor()
        # book title search
        cursor.execute("SELECT id, title, isbn, publication_date, availability FROM books WHERE title = %s",
        (title,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return Book(id = result[0], title = result[1], isbn = result[2], publication_date = result[3],
                availability = result[4])
        return None


    def __str__(self):
        status = "Available" if self.available == True else "Borrowed"
        return f"\nTitle: {self.title} - Author: {self.author} - Genre: {self.genre}\nPublication Date: {self.publication_date} - Status: {status}"

class User:
# structures user info neatly, has borrow and return functionalities for the user
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def __str__(self):
        return f"\nUser Name: {self.name} - Library ID: {self.library_id}\n{self.name}'s Borrowed Books: {','.join(self.borrowed_books) or 'N/A'}"
    
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
    def __init__(self, name, biography = None, id = None):
        self.id = id
        self.name = name
        self.biography = biography
# saves author details to database either by updating it if it exists or adding it to the authors table
    def save_author(self):
        conn = connect_database()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE authors SET name = %s, biography = %s WHERE id = %s", (self.name, self.biography, self.id))
        else:
            cursor.execute("INSERT INTO authors (name, biography) VALUES (%s, %s)", (self.name, self.biography))
        self.id = cursor.lastrowid
# committing the changes and closing cursor and connection
        conn.commit()
        cursor.close()
        conn.close()
    
    def search_author_name(self, name):
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, biography FROM authors WHERE name = %s", (name,))
        result = cursor.fetchchone()
        cursor.close()
        conn.close()
        if result:
            return Author(id = result[0], name = result[1], biography = result[2])
        return None

    def get_all_authors(self):
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, biography FROM authors")
        authors = cursor.fetchall()
        cursor.close()
        conn.close()
        return for author in authors:
            Author(id = author[0], name = author[1], biography = author[2])

    def __str__(self):
        return f"\nAuthor: {self.name} - Biography: {self.biography}"
        