Mini-Project: Library Management System with Database Integration

--- Decription ---
Integrating a MySQL database with Python to develop an advanced Library Management System, this command-line-based application is designed to streamline the management of books and resources within a library. 

--- Features ---
Same user interference and features listed below for inital project Library Management System but with added functionality to interact with the MySQL database 'library_db'

--- Database 'library_db' Layout ---
create database library_db;
USE library_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
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

--- Installation: ---
Prerequisites
Ensure you have the following installed on your machine:
- Python 3.8+
- pip (Python package installer)
- Virtual environment tool (recommended)

Steps
1. Clone the repository
Open your terminal and run:
git clone <https://github.com/codenamehenny/LibraryMngmtProject.git>

2. Create a virtual environment
It's recommended to create a virtual environment to manage dependencies:
python -m venv venv
source venv/bin/activate (For Windows use 'venv\Scripts\activate)

3. Install dependencies
Once the virtual environment is activated, install the required packages:
pip install -r requirements.txt

4. Set up environment variables (if any)
If the project uses environment variables, create a .env file in the project root and define them there. 
An example is provided:
cp .env.examples .env

Usage
Once installed, you can run the Library Management Project by executing the following command:
python main.py --input-file data/input.csv --output-file date/output.csv -- operation clean

Example
To clean the dataset and generate a cleaned output CSV:
python main.py --input-file data/raw_data.csv --ouput-file data/cleaned_data.csv --operation clean

For more options and help:
python main.py --help

--- Project Structure ---
LibraryMngmtProject
    - main.py (user interactions)
    - library_classes.py (book, user and author classes)
    - library_ops.py (all functions for book, user and author menues)

--- Running Tests ---
We use pytest for testing. To run the tests, use the following command:
pytest tests/
To check code for coverage, run:
pytest --cov=src tests/

--- Contributing ---
1. Fork the repository.
2. Create a branch: git checkout -b feature/your-feature-name.
3. Make your changes and commit: git commit -m 'Add some feature'
4. Push to the branch: git push origin feature/your-feature-name
5. Submit a pull request.

--- Guidelines ---
- Follow PEP 8 for Python code style
- Write tests for any new functionality
- Ensure all tests pass before submitting a pull request

--- Contact ---
For any questions, please reach out via 'genesis09m@hotmail.com'



---  Foundational Project Name: Library Management System ---
These were the inital project details and was used a building block for incorpating database integration

--- Description: ---
This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.

--- Features: ---
Enhanced User Interface (UI) and Menu for:
- Book Operations (add, borrow, return, search, and display)
- User Operations (add, view user details and display all users)
- Author Operations (add, view author details, and display all authors)

Class Structure:
- Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.
- User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
- Author: A class representing book authors with attributes like name and biography.

Encapsulation - defining private attributes and using getters and setters for necessary data access.

Modules - promoting code organization and maintainability. Create separate modules for classes, user interactions, and error handling.

Menu Actions:
• Adding a new book with all relevant details.
• Allowing users to borrow a book, marking it as "Borrowed."
• Allowing users to return a book, marking it as "Available."
• Searching for a book by its unique identifier (title) and displaying its details.
• Displaying a list of all books with their unique identifiers.
• Adding a new user with user details.
• Viewing user details.
• Displaying a list of all users.
• Adding a new author with author details.
• Viewing author details.
• Displaying a list of all authors.
• Quitting the application.

Error Handling - Using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.
