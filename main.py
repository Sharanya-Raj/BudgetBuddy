from user import User
from datetime import datetime, timedelta
import matplotlib.pyplot as myPlot

if __name__ == "__main__":
    #Defining all of possible userActions
    expenseType = ["Housing", "Utilities", "Groceries", "Dining Out", "Entertainment", "Transportation", "Miscellaneous"]
    revenueType = ["Salary", "Freelance Work", "Investment Gains", "Gifts", "Miscellaneous"]
    def transactionTracker(typeDict):
        '''Displays all transactions in the given dictionary (revenue/expense).'''
        for transaction in typeDict:
            print(transaction+": $"+str(typeDict[transaction]),end="\n")
        if len(typeDict) == 0:
            print("No data for graph.")
        else:
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
    
    def recordData(typeDict, transactionType, amount):
        '''Records a new transaction by updating the appropriate dictionary.'''
        if transactionType in typeDict:
            typeDict[transactionType] += amount
        else:
            typeDict[transactionType] = amount
    def totalCalculator(typeDict):
        '''Calculates the total of all transactions in the given dictionary.'''
        return sum(typeDict.values())

    def connect_with_NJIT_resources(help_category):
        '''Provides NJIT resources based on the help category.'''
        if help_category == "FINANCIAL_AID":
            return "Contact the Office of Student Financial Aid Services (SFAS) for FAFSA, grants, loans, scholarships, and special circumstances appeals."
        elif help_category == "BILLING_PAYMENTS":
            return "Contact the Office of the Bursar for your eStatement, payment plans, account holds, and tuition refunds."
        elif help_category == "EMERGENCY_FINANCE":
            return "Apply for the Highlander Student Emergency Fund through the Student Financial Aid Services Office for immediate, unexpected financial hardship."
        else:
            return "Please specify if your question is about FINANCIAL_AID, BILLING_PAYMENTS, or EMERGENCY_FINANCE to connect you with the right resource."
    
        
    def budgetAdvisor(income, expenses):
        '''Provides budget advice based on income and expenses.'''
        if expenses > income:
            return "Your expenses exceed your income. Consider reducing non-essential spending."
        elif expenses == income:
            return "Your expenses match your income. Try to save a portion of your income."
        else:
            return "Great job! Your income exceeds your expenses. Consider investing or saving the surplus."
    
    def recurringAlerts():
        """Check bills in user.recurringBills and alert if due within 3 days"""
        today = datetime.today().date()
        alert_threshold = today + timedelta(days=3)
        if len(user.recurringBills) == 0:
            print("No recurring bills found.")
            return

        for bill in user.recurringBills:
            bill_name= bill[0]
            amount = bill[1]
            due_date_str = bill[2]
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            if today <= due_date and due_date <= alert_threshold:
                print(f"Alert: '{bill_name}' of ${amount:.2f} is due on {due_date}")

    def addRecurringBill(bill_name, amount, due_date):
        """Add a new recurring bill to user.recurringBills"""
        user.recurringBills.append([bill_name, amount, due_date])

    def removeRecurringBill(self, bill_name):
        """Remove a recurring bill from suser.recurringBills by name"""
        for bill in user.recurringBills:
            if bill[0] == bill_name:
                user.recurringBills.remove(bill)
                print(f"Removed recurring bill: {bill_name}")
                return
        print(f"No recurring bill found with the name: {bill_name}")
    
    
    
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

    print(f"Welcome, {user.userName}! Here are the available actions you can perform:")

    #Displaying available actions
    listActions = ["transactionTracker", "recordData", "totalCalculator", "connect_with_NJIT_resources", "budgetAdvisor","recurringAlerts", "addRecurringBill","removeRecurringBill"] 
    
    count = 1
    for action in listActions:
        print("\n" + str(count) + ". " + action)
        count += 1
    input_action = input("Enter an action to perform: Note that it is recommended to utilize \"transaction tracker\" to view pasts transactions before using this function, as your changes will affect past recorded data. Treat information stored in transactionTracker as amounts for the month (according to your personal budgeting), not cumulative totals.")

    #Utilizing transactionTracker
    if input_action == "transactionTracker":
        revExp = input("Do you want to track 'revenue' or 'expense' transactions? ").lower()
        if revExp == "revenue":
            transactionTracker(user.income)
        elif revExp == "expense":
            transactionTracker(user.expenses)
        else:
            print("Invalid input. Please enter 'revenue' or 'expense'. Another incorrect response will exit the program.")
            revExp = input("Do you want to track 'revenue' or 'expense' transactions? ").lower()
            if revExp == "revenue":
                transactionTracker(user.income)
            else:
                transactionTracker(user.expenses)
    
    #Utilizing recordData
    elif input_action == "recordData":
        revExp = input("Do you want to record a 'revenue' or 'expense' transaction? ").lower()
        if revExp == "revenue":
            transactionType = input("Enter the type of transaction. Current types are: " + str(user.revenueType) + ": ")
            amount = float(input("Enter the amount in dollars. If a previously recorded transaction exists, this amount will be added to it (or substracted if negative number entered). Else, this amount will serve as the starting value: "))
            user.recordData(user.income, transactionType, amount)
        elif revExp == "expense":
            transactionType = input("Enter the type of transaction. Current types are: " + str(user.expenseType) + ": ")
            amount = float(input("Enter the amount in dollars. If a previously recorded transaction exists, this amount will be added to it (or substracted if negative number entered). Else, this amount will serve as the starting value: "))
            user.recordData(user.expenses, transactionType, amount)
        else:
            print("Invalid input. Please enter 'revenue' or 'expense'. Another incorrect response will exit the program.")
            revExp = input("Do you want to record a 'revenue' or 'expense' transaction? ").lower()
            if revExp == "revenue":
                transactionType = input("Enter the type of transaction. Current types are: " + str(user.income.keys()) + ": ")
                amount = float(input("Enter the amount in dollars. If a previously recorded transaction exists, this amount will be added to it (or substracted if negative number entered). Else, this amount will serve as the starting value: "))
                user.recordData(user.income, transactionType, amount)
            elif revExp == "expense":
                transactionType = input("Enter the type of transaction. Current types are: " + str(user.expenses.keys()) + ": ")
                amount = float(input("Enter the amount in dollars. If a previously recorded transaction exists, this amount will be added to it (or substracted if negative number entered). Else, this amount will serve as the starting value: "))
                user.recordData(user.expenses, transactionType, amount)
            else:
                print("Invalid input. Exiting program.")
    
    #Utilizing totalCalculator
    elif input_action == "totalCalculator":
        revExp = input("Do you want to calculate total 'revenue' or 'expense' transactions? ").lower()
        if revExp == "revenue":
            total_income = user.totalCalculator(user.income)
            print(f"Total revenue: ${total_income:.2f}")
        elif revExp == "expense":
            total_expenses = user.totalCalculator(user.expenses)
            print(f"Total expenses: ${total_expenses:.2f}")
        else:
            print("Invalid input. Please enter 'revenue' or 'expense'. Another incorrect response will exit the program.")
            revExp = input("Do you want to calculate total 'revenue' or 'expense' transactions? ").lower()
            if revExp == "revenue":
                total_income = user.totalCalculator(user.income)
                print(f"Total revenue: ${total_income:.2f}")
            else:
                total_expenses = user.totalCalculator(user.expenses)
                print(f"Total expenses: ${total_expenses:.2f}")
    
    #Utilizing connect_with_NJIT_resources
    elif input_action == "connect_with_NJIT_resources":
        help_category = input("Enter help category (FINANCIAL_AID, BILLING_PAYMENTS, EMERGENCY_FINANCE): ").upper()
        resource_info = user.connect_with_NJIT_resources(help_category)
        print(resource_info)
    
    #Utilizing budgetAdvisor
    elif input_action == "budgetAdvisor":
        advice = user.budgetAdvisor(user.totalCalculator(user.income), user.totalCalculator(user.expenses))
        print(advice)
    
    #Utilizing recurringAlerts
    elif input_action == "recurringAlerts":
        user.recurringAlerts()
    
    #Utilizing addRecurringBill
    elif input_action == "addRecurringBill":
        bill_name = input("Enter the name of the recurring bill: ")
        amount = float(input("Enter the amount of the bill in dollars: "))
        due_date = input("Enter the due date of the bill (YYYY-MM-DD): ")
        user.addRecurringBill(bill_name, amount, due_date)
        print(f"Added recurring bill: {bill_name}, Amount: ${amount:.2f}, Due Date: {due_date}")
    
    #Utilizing removeRecurringBill
    elif input_action == "removeRecurringBill":
        bill_name = input("Enter the name of the recurring bill to remove: ")
        user.removeRecurringBill(bill_name)
    
    else:
        print("Invalid action selected. Exiting program.")

    
    
    