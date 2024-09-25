# user interaction file with all menues

import library_ops as ops

def main_system():
    while True:
        try:
            print("\nWelcome to the Library Management System!\nMain Menu:")
            print("1. Book Operations\n2. User Operations\n3. Author Operations \n4. Quit")
            option = int(input("Enter option number here: "))
            if option == 1:
                book_menu()
            elif option ==  2:
                user_menu()
            elif option == 3:
                author_menu()
            elif option == 4:
                print("Quitting...")
                break
            else:
                print("\nEnter a valid number between 1-4")
        except ValueError:
            print("Please enter a valid number")
        except Exception as e:
            print(f"Error message: '{e}'. Please try again")
        finally:
            print("Thanks for using the library management system!")

def book_menu():
    while True:
        try:
            print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book")
            print("4. Search for a book\n5. Display all books\n6. Return to Main Menu")
            option = int(input("Enter option: "))
            if option == 1:
                ops.add_book()
            elif option == 2:
                ops.borrow_book()
            elif option == 3:
                ops.return_book()
            elif option == 4:
                ops.search_book()
            elif option == 5:
                ops.display_books()
            elif option == 6:
                print("Returning to main menu...")
                break
            else:
                print("Please enter a valid number between 1-6")
        except ValueError:
            print("Please enter a valid number between 1-6")
        except Exception as e:
            print(f"Error message: '{e}'. Please try again")

def user_menu():
    while True:
        try:
            print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Back to Main Menu")
            option = int(input("Enter option: "))
            if option == 1:
                ops.add_user()
            elif option == 2:
                ops.view_user()
            elif option == 3:
                ops.display_users()
            elif option == 4:
                print("Returning to main menu...")
                break
            else:
                print("Please enter a number between 1-4")
        except ValueError:
            print("Please enter a valid number between 1-4")
        except Exception as e:
            print(f"Error message: '{e}'. Please try again")

def author_menu():
    while True:
        try:
            print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Back to Main Menu")
            option = int(input("Enter option: "))
            if option == 1:
                ops.add_author()
            elif option == 2:
                ops.view_author()
            elif option == 3:
                ops.display_authors()
            elif option == 4:
                print("Returning to main menu...")
                break
            else:
                print("Please enter a number between 1-4")
        except ValueError:
            print("Please enter a valid number between 1-4")
        except Exception as e:
            print(f"Error message: '{e}'. Please try again")
if __name__ == "__main__":
    main_system()