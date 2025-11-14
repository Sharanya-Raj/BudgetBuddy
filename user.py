import csv
class User:
    def __init__(self, userName, password, email, studentNJIT, newAcct):
        '''Initialize a new user object according to either new or past data and save to userData.csv'''
        inputUserData = [userName, password, email, studentNJIT]
        infile = open('userData.csv', mode = "r")
        while True:
            infile.seek(0)  # Go back to start of file
            conflict_found = False
            for row in infile:
                user_data = row.strip().split(',')  # [username, password, email, studentNJIT, income, expenses]
                
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
                            self.income = user_data[4]
                            self.expenses = user_data[5]
                            print("Loaded existing user.")
                            return
                        else:
                            pchange = input("Incorrect password. Would you like to change your password? (yes/no): ")
                            if pchange.lower() == "yes":
                                email = input("Enter your email: ")
                                self.change_password(email, inputUserData[0])
                            else:
                                print("Exiting program.")
                                return

            if not conflict_found:
                if newAcct:
                    self.userName = userName
                    self.password = self.valid_password(password)
                    self.email = email
                    studentNJIT_input = input("Are you a NJIT student? (yes/no): ").lower()
                    if studentNJIT_input != "yes" and studentNJIT_input != "no":
                        while studentNJIT_input != "yes" and studentNJIT_input != "no":
                            studentNJIT_input = input("Invalid input. Are you a NJIT student? (yes/no): ").lower()
                    elif studentNJIT_input == "yes":
                        self.studentNJIT = True
                    else:
                        self.studentNJIT = False
                    self.income = {0}
                    self.expenses = {0}
                    opened_file = open('userData.csv', mode = "a", newline ='')
                    opened_file.write(f"{self.userName},{self.password},{self.email},{self.studentNJIT},{self.income},{self.expenses}\n")
                    opened_file.close()
                else:
                    print("Invalid credentials. Exiting program.")
                return

    def valid_password(self,password):
        '''Check if the password meets the required criteria'''
        valid = (len(password)>=8, "\'!@#$%^&*()-_+=\'" in password, any(char.isdigit() for char in password), any(char.isupper() for char in password), any(char.islower() for char in password))
        if valid:
            return password
        else:
            print("Password must be at least 8 characters long, include a special character, a number, an uppercase letter, and a lowercase letter.")
            password = input("Enter a new password. It must be at least 8 characters, and include a special character, a number, an uppercase letter, and a lowercase letter: ")
            valid = (len(password)>=8, any(char in '\'!@#$%^&*()-_+=\'' for char in password), any(char.isdigit() for char in password), any(char.isupper() for char in password), any(char.islower() for char in password))
        return password
    
    def change_password(self, email, username):
        '''Change the user's password after verifying email and username'''
        if self.email == email and self.userName == username:
            new_password = self.valid_password(input("Enter your new password: "))
            print("Password changed successfully.")
        else:
            print("Email or username does not match our records.")