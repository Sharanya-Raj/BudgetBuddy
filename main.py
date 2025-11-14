acct = int(input("Login or Setup Account? (1 for Login, 2 for Setup) : "))
while acct != 1 and acct != 2:
    print("Invalid option. Please enter 1 for Login or 2 for Setup.")
    acct = int(input("Login or Setup Account? (1 for Login, 2 for Setup) : "))
if acct == 1:
    # Login
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    if user.login(userName, password):
        print("Login successful!")
    else:
        print("Login failed.")
else:
    # Setup Account
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    studentNJIT = input("Are you a student at NJIT? (yes/no): ").lower() == "yes"
    user = User().initUser(userName, password, email, studentNJIT)
    print("Account setup successful!")
