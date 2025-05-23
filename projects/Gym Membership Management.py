import os
import time

def clear_screen():
    os.system('cls' if os.name == "nt" else 'clear')

class User:
    def __init__(self, first_name, last_name, ID, status='inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.status = status if status else 'inactive'
    def display_users(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Membership ID: {self.ID}")
        print(f"Membership Status: {self.status}")
        print('_' * 20)

def create_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    ID = input("Enter membership ID: ")
    status = input("Enter membership status, or press Enter to skip: ")
    return User(first_name, last_name, ID, status)

new_users = []

while True:
    clear_screen()
    print("\nWelcome to Gym Membership Management\n")
    print("""
    Choose an action:

    1. Add new user
    2. Display all users
    3. Search for a member
    4. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        clear_screen()
        new_users.append(create_user())
        print("User added successfully")
        time.sleep(2)

    elif choice == '2':
        clear_screen()
        if new_users:
            print("Displaying all new users ......")
            time.sleep(1)
            for user in new_users:
                user.display_users()
            time.sleep(5)
        else:
            print("Sorry, didn't find any user to display.")
            time.sleep(2)

    elif choice == '3':
        clear_screen()
        print("""
        Search by:

        1. Membership ID
        2. First Name
        3. Membership Status
        """)
        choice2 = input("Enter your choice: ")

        if choice2 == '1':
            ID1 =input('Enter the membership ID to search: ')
            clear_screen()
            there = False
            for user in new_users:
                if user.ID == ID1:
                    user.display_users()
                    there = True
                    break
            if not there:
                print("User not found.")
            time.sleep(2)

        elif choice2 == '2':
            first_name = input("Enter the first name to search: ")
            clear_screen()
            there = False
            for user in new_users:
                if user.first_name.lower() == first_name.lower():
                    user.display_users()
                    there = True
            if not there:
                print("User not found.")
            time.sleep(2)

        elif choice2 == '3':
            status = input("Enter the membership status to search (active/inactive): ")
            clear_screen()
            there = False
            for user in new_users:
                if user.status.lower() == status.lower():
                    user.display_users()
                    there = True
            if not there:
                print("User not found.")
            time.sleep(2)

    elif choice == '4':
        print("Exiting ....")
        break

    else:
        print("Invalid choice! Please try again.")
        time.sleep(2)
