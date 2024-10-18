# this file has all the classes (book, user, and author)
# the classes have been updated with database integration
from connect_db import connect_database
from datetime import date

class Book:
    # structures user inputs for book info neatly
    def __init__(self, title, author, isbn, publication_date, availability = True, id = None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability

    def save_book(self):
        conn = connect_database()
        cursor = conn.cursor()
        # checking to see if author exists and saving the author first if it doesn't
        if not self.author.id:
            self.author.save_author()
        if self.id:
            cursor.execute("""
                UPDATE books SET title = %s, author_id = %s, isbn = %s, 
                publication_date = %s, availability = %s WHERE id = %s
                """, (self.title, self.author.id, self.isbn, self.publication_date, self.availability))
            print(f"Details for {self.title} updated successfully")
        else:
            cursor.execute("""
                INSERT INTO books (title, author_id, isbn, publication_date, availability)
                VALUES (%s, %s, %s, %s, %s)""",
                (self.title, self.author_id, self.isbn, self.publication_date, self.availability))
            self.id = cursor.lastrowid
            print(f"{self.title} added to library successfully.")
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
            return Book(id = result[0], title = result[1], isbn = result[2], publication_date = result[3], availability = result[4])
        return None

    def get_all_books(self):
        conn = connect_database()
        cursor = conn.cursor()
        # this combines the author and book tables
        cursor.execute("""
            SELECT b.id, b.title, a.id, a.biography, b.isbn, b.publication_date, b.availability
            FROM books b
            JOIN authors a ON b.author_id = a.id
        """)
        books = cursor.fetchall()

        cursor.close()
        conn.close()
        if books:
            book_list = []
            for book in books:
                author = Author(id = book[2], name = book[3], biography = book[4])
                book_list.append(Book(id = book[0], title = book[1], author = author, isbn = book[5],
                    publication_date = book[6], availability = book[7]))
            return book_list
        return []

    def mark_as_borrowed(self, user_id):
        conn = connect_database()
        cursor = conn.cursor()
        # checking out the book by adding it to the borrowed books table
        cursor.execute("""
            INSERT INTO borrowed_books (user_id, book_id, borrowed_date)
            VALUES (%s, %s, %s)""",
            (user_id, self.id, date.today()))
        # changing book availability status to False
        cursor.execute("UPDATE books SET availability = %s WHERE id = %s",
            (False, self.id))
        print(f"{self.id} successfully marked borrowed by library id {user_id}")

        conn.commit()
        cursor.close()
        conn.close()
       
    def return_book(self, user_id):
        conn = connect_database()
        cursor = conn.cursor()
        # updating return date for the borrowed book
        cursor.execute("""
            UPDATE borrowed_books
            SET return_date = %s
            WHERE user_id = %s AND book_id = %s AND return_date IS NULL""",
            (date.today(), user_id, self.id))
        # updating book availability to True
        cursor.execute("UPDATE books SET availability = %s WHERE id = %s",
            (True, self.id))

        conn.commit()
        cursor.close()
        conn.close()

    def __str__(self):
        status = "Available" if self.available == True else "Borrowed"
        return f"\nTitle: {self.title} - Author: {self.author} - ISBN: {self.isbn}\nPublication Date: {self.publication_date} - Status: {status}"

class User:
    # structures user info neatly, has borrow and return functionalities for the user
    def __init__(self, name, library_id, id = None):
        self.name = name
        self.library_id = library_id
       
    def __str__(self):
        return f"\nUser Name: {self.name} - Library ID: {self.library_id}\n{self.name}'s Borrowed Books: {','.join(self.borrowed_books) or 'N/A'}"
    
    def save_user(self):
        conn = connect_database()
        cursor = conn.cursor()
        # checks if the user is registered, updates info if it is or adds it to the Users table if it isn't
        if self.id:
            cursor.execute("UPDATE users SET name = %s, library_id = %s WHERE id = %s",
                (self.name, self.library_id, self.id))
            print(f"Profile for user {self.name} has been updated")
        else:
            cursor.execute("INSERT INTO users (name, library_id) VALUES (%s, %s)",
                (self.name, self.library_id))
            self.id = cursor.lastrowid
            print(f"{self.name} has been added successfully")

        conn.commit()
        cursor.close()
        conn.close()

    def search_by_library_id(self, library_id):
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, library_id FROM users WHERE library_id = %s", (library_id,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return User(id = result[0], name = result[1], library_id = result[2])
        return f"{library_id} not found"

    def get_all_users(self):
        conn = connect_database()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, library_id FROM users")
        users = cursor.fetchall()

        cursor.close()
        conn.close()

        if users:
            return for user in users:
                [User(id = user[0], name = user[1], library_id = user[2])]
        else:
            return "No users registered"

    def get_borrowed_books(self):
        conn = connect_database()
        cursor = conn.cursor()
        # getting all the borrowed books by a user, grabbing info from users table and borrowed books table
        cursor.execute("""
            SELECT b.id, b.title, a.id, a.name, a.biography, b.isbn, b.publication_date
            FROM borrowed_books bb
            JOIN books b ON bb.book_id = b.id
            JOIN authors a ON b.author_id = a.id
            WHERE bb.user_id %s and bb.return_date IS NULL
            """, (self.id,))
        books = cursor.fetchall()
        
        cursor.close()
        conn.close()

        borrowed_books = []
        if books:
            for book in books:
                author = Author(id = book[2], name = book[3], biography = book[4])
                borrowed_books.append(Book(id = book[0], title = book[1], author = author, isbn = book[5], 
                  publication_date = book[6], availability = False))
            return borrowed_books
        return []

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

        if authors:
            return for author in authors:
                Author(id = author[0], name = author[1], biography = author[2])
        return None

    def __str__(self):
        return f"\nAuthor: {self.name} - Biography: {self.biography}"
        