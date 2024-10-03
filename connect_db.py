# this file establishes connection to the 'library_db' database which manages the library
import mysql.connector
from mysql.connector import Error

def connect_database():
    # Database connection parameters
    db_name = "library_db"
    user = "root"
    password = " "
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print(f"Connected to MYSQL '{db_name}' successfully")
    except Error as e:
        print(f"Error Message: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("MYSQL connection is now closed.")