def main_system():
    while True:
        try:
            print("\nWelcome to the Library Management System!\nMain Menu:")
            print("1. Book Operations\n2. User Operations\n3. Author Operations \n4. Quit")
            main_menu_option = int(input("Enter option number here: "))
            if main_menu_option == 1:
                print("Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book")
                print("4. Search for a book\n5. Display all books\n6. Back to Main Menu")
            elif main_menu_option ==  2:
                print("User Operations:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Back to Main Menu")
            elif main_menu_option == 3:
                print("Author Operations:\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Back to Main Menu")
            elif main_menu_option == 4:
                print("Quitting...")
                break
            else:
                print("\nEnter a valid number between 1-4")
        except ValueError:
            print("Please Enter a valid number")
        except Exception as e:
            print(f"Error message: '{e}'. Please try again")

main_system()