from user import User

if __name__ == "__main__":
    # Main program to handle user login and account setup
    acct = input("Do you have an existing account? (yes/no): ").lower()
    while acct != "yes" and acct != "no":
        acct = input("Invalid input. Do you have an existing account? (yes/no): ").lower()
    userName = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = User(userName, password, email, False, False)  # Email and studentNJIT are not needed for login