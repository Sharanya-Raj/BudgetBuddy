from user import User


if __name__ == "__main__":
    global expenseType 
    expenseType = ["Housing", "Utilities", "Groceries", "Dining Out", "Entertainment", "Transportation", "Miscellaneous"]
    global revenueType 
    revenueType = ["Salary", "Freelance Work", "Investment Gains", "Gifts", "Miscellaneous"]
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
    input_action = input("Enter an action to perform: Note that it is recommended to utilize \"transaction tracker\" to view pasts transactions before using this function, as your changes will affect past recorded data. Treat information stored in transactionTracker as amounts for the month (according to your personal budgeting), not cumulative totals. \n")

    #Utilizing transactionTracker
    if input_action == "transactionTracker":
        revExp = input("Do you want to track 'revenue' or 'expense' transactions? ").lower()
        if revExp == "revenue":
            user.transactionTracker(user.income)
        elif revExp == "expense":
            user.transactionTracker(user.expenses)
        else:
            print("Invalid input. Please enter 'revenue' or 'expense'. Another incorrect response will exit the program.")
            revExp = input("Do you want to track 'revenue' or 'expense' transactions? ").lower()
            if revExp == "revenue":
                user.transactionTracker(user.income)
            else:
                user.transactionTracker(user.expenses)
    
    #Utilizing recordData
    elif input_action == "recordData":
        revExp = input("Do you want to record a 'revenue' or 'expense' transaction? ").lower()
        user.recordData(revExp)
    
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
        user.recurringAlerts(user.recurringBills)
    
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


    
    
    