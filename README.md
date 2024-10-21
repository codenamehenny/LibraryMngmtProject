Library Management System with MySQL Integration

This project is Library Management System that uses a MySQL database for managing information about books, users, and authors. The system allows users to perform various operations such as adding books, borrowing and returning books, viewing users, and managing author information.

~ Project Structure ~
Here's the project directory:
1. main.py: This user interaction file that contains the main menu and manages uer inputs to navigate the system. It is the entry point of the system. It handles all user interactions, displaying menus for managing books, users and authors. It routes user inputs to appropriate functions in library_ops.py and provides feedback based on user actions.

2. connect_db.py: Establishes a connection to the MySQL database (library_db), which stores and manages all the system's data. It includes error handling to manage connection issues gracefully.

3. library_classes.py: Contains the core classes (Book, User, Author) that represent the library entities and handle database interactions

4. library_ops.py: Contains the operations that map user inputs from main.py to actions such as adding, viewing, borrowing, and returning books.

~ Features ~ 
1. Book Operations:
    - add new books
    - borrow a book
    - return a book
    - search for a book by title
    - display all available books
2. User Operations:
    - add new users
    - view user details
    - display all users
3. Author Operations:
    - add new authors
    - view author details
    - display all author 

~ Prerequisites ~
To run this project, you'll need to have the following installed on your system:
1. Python 3.x: The programming language used for the application.
2. MySQL: The database system used for storing library information.
3. MySQL Connector: Python library to connect to MySQL

To install the MySQL Connector, run:
    pip install mysql-connector-python

~ Installation and Setup ~
1. Clone the repository:
    git clone https://github.com/codenamehenny/LibraryMngmtProject.git
    cd LibraryMngmntProject
2. Set up the MySQL Database:
    - Open MySQL and run the following commands to create he database and tables:
    CREATE DATABASE library_db;
    USE library_db;

    CREATE TABLE authors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        biography TEXT
    );

    CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author_id INT,
        isbn VARCHAR(13) NOT NULL,
        publication_date DATE,
        availability BOOLEAN DEFAULT 1,
        FOREIGN KEY (author_id) REFERENCES authors(id)
    );

    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        library_id VARCHAR(10) NOT NULL UNIQUE
    );

    CREATE TABLE borrowed_books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        book_id INT,
        borrow_date DATE NOT NULL,
        return_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    );

3. Configure Database Connection:
    - Open the connect_db.py file and configure the connection details:
    # connect_db.py
    def connect_database():
        db_name = "library_db"
        user = "root"  # Your MySQL username
        password = "your_password"  # Your MySQL password
        host = "127.0.0.1"  # Localhost

4. Run the Application:
    - After setting up the database, you can run the application with:
    python main.py

~ Error Handling ~
The project uses try-except blocks to manage potential errors including:
    - Invalid input, like entering text where a number is expected
    - Database connection errors
    - Duplicate user IDs or book issues

~ Contribution ~ 
Feel free to fork this repository and make improvements. Pull requests are welcomed
To contribute:
1. Fork the repository
2. Create a new branch for your feature:
    git checkout -b feature-name
3. Make your changes and commit:
    git commit -m 'Add feature'
4. Push to your branch:
    git push origin feature-name
5. Open a pull request on Github