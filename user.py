import csv
import sys
class User:
    global expenseType 
    expenseType = ["Housing", "Utilities", "Groceries", "Dining Out", "Entertainment", "Transportation", "Miscellaneous"]
    global revenueType 
    revenueType = ["Salary", "Freelance Work", "Investment Gains", "Gifts", "Miscellaneous"]
    def __init__(self, userName, password, email, studentNJIT, newAcct):
        
        '''Initialize a new user object according to either new or past data and save to userData.csv'''
        # Ensure attributes exist before any branch logic uses them
        self.userName = None
        self.password = None
        self.email = None
        self.studentNJIT = None
        self.income = {}
        self.expenses = {}
        self.recurringBills = []
        inputUserData = [userName, password, email, studentNJIT]
        infile = open('userData.csv', mode = "r")
        while True:
            infile.seek(0)  # Go back to start of file
            conflict_found = False
            for row in infile:
                user_data = row.strip().split(',')  # [username, password, email, studentNJIT, income, expenses, bills]
                
                # Check for email conflict
                if newAcct and inputUserData[2] == user_data[2]:
                    print("Email already exists. Please use a different email.")
                    inputUserData[2] = input("Enter a new email: ")
                    conflict_found = True
                    break  # Restart loop with new email

                if inputUserData[0] == user_data[0]:
                    if newAcct:
                        print("Username already exists. Please choose a different username.")
                        inputUserData[0] = input("Enter a new username: ")
                        conflict_found = True
                        break  # Restart loop with new username
                    else:
                        if inputUserData[0] == user_data[0] and inputUserData[1] == user_data[1]:
                            self.userName = user_data[0]
                            self.password = user_data[1]
                            self.email = user_data[2]
                            self.studentNJIT = user_data[3]
                            self.income = eval(user_data[4])
                            self.expenses = eval(user_data[5])
                            # Do not reference self.user (it doesn't exist). Keep bills on self.
                            self.recurringBills = []
                            print("Loaded existing user.")
                            return
                        else:
                            pchange = input("Incorrect password. Would you like to change your password? (yes/no): ")
                            if pchange.lower() == "yes":
                                email = input("Enter your email: ")
                                self.change_password(email, inputUserData[0])
                            else:
                                print("Exiting program.")

                                sys.exit()

            # If conflicts were found, restart and re-check uniqueness with updated inputs
            if conflict_found:
                continue

            # No conflicts across file; proceed
            if newAcct:
                # Validate password using provided password
                self.password = self.valid_password(inputUserData[1])
                # Validate studentNJIT input
                studentNJIT_input = input("Are you a NJIT student? (yes/no): ").lower()
                while studentNJIT_input not in ("yes", "no"):
                    studentNJIT_input = input("Invalid input. Are you a NJIT student? (yes/no): ").lower()

                # Finalize user fields
                self.userName = inputUserData[0]
                self.email = inputUserData[2]
                self.studentNJIT = (studentNJIT_input == "yes")

                # Initialize income/expenses categories
                for transaction in revenueType:
                    self.income[transaction] = 0
                for transaction in expenseType:
                    self.expenses[transaction] = 0
                self.recurringBills = []

                # Append only after validations and uniqueness
                opened_file = open('userData.csv', mode = "a", newline ='')
                opened_file.write(f"{self.userName},{self.password},{self.email},{self.studentNJIT},{self.income},{self.expenses}\n")
                opened_file.close()
                return
            else:
                print("Invalid credentials. Exiting program.")
                sys.exit()

    def valid_password(self,password):
        '''Check if the password meets the required criteria'''
        has_len = len(password) >= 8
        has_special = any(char in "'!@#$%^&*()-_+='" for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        valid = has_len and has_special and has_digit and has_upper and has_lower
        if valid:
            return password
        else:
            print("Password must be at least 8 characters long, include a special character, a number, an uppercase letter, and a lowercase letter.")
            password = input("Enter a new password. It must be at least 8 characters, and include a special character, a number, an uppercase letter, and a lowercase letter: ")
            has_len = len(password) >= 8
            has_special = any(char in "'!@#$%^&*()-_+='" for char in password)
            has_digit = any(char.isdigit() for char in password)
            has_upper = any(char.isupper() for char in password)
            has_lower = any(char.islower() for char in password)
        return password
    
    def change_password(self, email, username):
        '''Change the user's password after verifying email and username'''
        if self.email == email and self.userName == username:
            new_password = self.valid_password(input("Enter your new password: "))
            print("Password changed successfully.")
        else:
            print("Email or username does not match our records.")