import csv
import sys
import matplotlib.pyplot as myPlot
from datetime import datetime, timedelta
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
                user_data = row.split('\t')  # [username, password, email, studentNJIT, income, expenses, bills]
                
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
                opened_file.write(f"{self.userName}\t{self.password}\t{self.email}\t{self.studentNJIT}\t{str(self.income)}\t{str(self.expenses)}\t{self.recurringBills}\n")
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
    
    
    #Defining all of possible userActions
    
    def transactionTracker(self,typeDict):
        '''Displays all transactions in the given dictionary (revenue/expense).'''
        
        if len(typeDict) == 0:
            print("No current data. ")
        else:
            for transaction in typeDict:
                print(transaction+": $"+str(typeDict[transaction])+"\n")
            plotLabels = list(typeDict.keys())
            plotValues = list(typeDict.values())
            myPlot.figure(figsize=(7,4))
            myPlot.bar(plotLabels, plotValues)
            myPlot.title("Transaction Overview")
            myPlot.xlabel("Category")
            myPlot.ylabel("Amount ($)")
            myPlot.xticks(rotation = 45)
            myPlot.tight_layout()
            myPlot.show()
    
    def recordData(self, typeDict):
        '''Records a new transaction by updating the appropriate dictionary.'''
        if typeDict == "revenue":
            transactionType = input("Enter the type of transaction. Current types are: " + str(revenueType) + ": ")
            if transactionType not in revenueType:
                print("Invalid transaction type. Please choose from the available types.")
                transactionType = input("Enter the type of transaction. Current types are: " + str(revenueType) + ". Another incorrect response will exit the program: ")
                if transactionType not in revenueType:
                    print("Invalid input. Exiting program.")
                    sys.exit()
            
            amt = float(input("Enter the amount in dollars. If a previously recorded transaction exists, this amount will be added to it (or substracted if negative number entered). Else, this amount will serve as the starting value: "))

            if transactionType in self.income:
                self.income[transactionType] += amt
            else:
                self.income[transactionType] = amt

        elif typeDict == "expense":
            transactionType = input("Enter the type of transaction. Current types are: " + str(expenseType) + ": ")
            if transactionType not in expenseType:
                print("Invalid transaction type. Please choose from the available types.")
                transactionType = input("Enter the type of transaction. Current types are: " + str(expenseType) + ". Another incorrect response will exit the program: ")
                if transactionType not in expenseType:
                    print("Invalid input. Exiting program.")
                    sys.exit()
            
            amt = float(input("Enter the amount in dollars. If a previously recorded transaction exists, this amount will be added to it (or substracted if negative number entered). Else, this amount will serve as the starting value: "))

            if transactionType in self.expenses:
                self.expenses[transactionType] += amt
            else:
                self.expenses[transactionType] = amt
        

        f = open('userData.csv', 'r')
        rows = f.readlines()
        f.close()

        i = 0
        while i < len(rows):
            line = rows[i].rstrip('\n')
            parts = line.split('\t')
            if parts[0] == self.userName:
                parts[1] = self.password
                parts[2] = self.email
                parts[3] = str(self.studentNJIT)
                parts[4] = str(self.income)
                parts[5] = str(self.expenses)
                parts[6] = str(self.recurringBills)
                rows[i] = '\t'.join(parts[:7]) + '\n'
                break
            i += 1

        f = open('userData.csv', 'w')
        j = 0
        while j < len(rows):
            f.write(rows[j])
            j += 1
        f.close()
    def totalCalculator(self, typeDict):
        '''Calculates the total of all transactions in the given dictionary.'''
        return sum(typeDict.values())

    def connect_with_NJIT_resources(self, help_category):
        if self.studentNJIT == False:
            return "This resource is only available to NJIT students."
        '''Provides NJIT resources based on the help category.'''
        if help_category == "FINANCIAL_AID":
            return "Contact the Office of Student Financial Aid Services (SFAS) for FAFSA, grants, loans, scholarships, and special circumstances appeals."
        elif help_category == "BILLING_PAYMENTS":
            return "Contact the Office of the Bursar for your eStatement, payment plans, account holds, and tuition refunds."
        elif help_category == "EMERGENCY_FINANCE":
            return "Apply for the Highlander Student Emergency Fund through the Student Financial Aid Services Office for immediate, unexpected financial hardship."
        else:
            return "Please specify if your question is about FINANCIAL_AID, BILLING_PAYMENTS, or EMERGENCY_FINANCE to connect you with the right resource."
    
        
    def budgetAdvisor(self, income, expenses):
        '''Provides budget advice based on income and expenses.'''
        if expenses > income:
            return "Your expenses exceed your income. Consider reducing non-essential spending."
        elif expenses == income:
            return "Your expenses match your income. Try to save a portion of your income."
        else:
            return "Great job! Your income exceeds your expenses. Consider investing or saving the surplus."
    
    def recurringAlerts(self, recurringBills):
        """Check bills in user.recurringBills and alert if due within 3 days"""
        today = datetime.today().date()
        alert_threshold = today + timedelta(days=3)
        if len(self.recurringBills) == 0:
            print("No recurring bills found.")
            return

        for bill in recurringBills:
            bill_name= bill[0]
            amount = bill[1]
            due_date_str = bill[2]
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            if today <= due_date and due_date <= alert_threshold:
                print(f"Alert: '{bill_name}' of ${amount:.2f} is due on {due_date}")

    def addRecurringBill(self,bill_name, amount, due_date):
        """Add a new recurring bill to user.recurringBills"""
        self.recurringBills.append([bill_name, amount, due_date])

    def removeRecurringBill(self, bill_name):
        """Remove a recurring bill from suser.recurringBills by name"""
        for bill in self.recurringBills:
            if bill[0] == bill_name:
                self.recurringBills.remove(bill)
                print(f"Removed recurring bill: {bill_name}")
                return
        print(f"No recurring bill found with the name: {bill_name}")
    
    