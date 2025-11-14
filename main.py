from user import User

if __name__ == "__main__":
    # Main program to handle user login and account setup
    acct = input("Do you have an existing account? (yes/no): ").lower()
    while acct != "yes" and acct != "no":
        acct = input("Invalid input. Do you have an existing account? (yes/no): ").lower()
    if acct == "no":
        newAcct = True
    else:
        newAcct = False
    email = input("Enter email: ")
    userName = input("Enter username: ")
    password = input("Enter password: ")
    user = User(userName, password, email, False, newAcct)