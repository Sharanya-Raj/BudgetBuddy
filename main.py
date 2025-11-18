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
    user = userActions(userName, password, email, False, newAcct)

    print(f"Welcome, {user.userName}!")

    #Displaying available actions
    listActions = ["transactionTracker", "recordData", "totalCalculator", "connect_with_NJIT_resources", "budgetAdvisor"] 
    for action in listActions:
        print(f"Available action: {action}")
    input_action = input("Enter an action to perform: ")

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
        if revExp == "revenue":
            transactionType = input("Enter the type of transaction. Current types are: " + str(user.income.keys()) + ": ")
            amount = float(input("Enter the amount in dollars: "))
            user.recordData(user.income, transactionType, amount)
        elif revExp == "expense":
            transactionType = input("Enter the type of transaction. Current types are: " + str(user.income.keys()) + ": ")
            amount = float(input("Enter the amount in dollars: "))
            user.recordData(user.income, transactionType, amount)
        else:
            print("Invalid input. Please enter 'revenue' or 'expense'. Another incorrect response will exit the program.")
            revExp = input("Do you want to record a 'revenue' or 'expense' transaction? ").lower()
            if revExp == "revenue":
                transactionType = input("Enter the type of transaction. Current types are: " + str(user.income.keys()) + ": ")
                amount = float(input("Enter the amount in dollars: "))
                user.recordData(user.income, transactionType, amount)
            else:
                transactionType = input("Enter the type of transaction. Current types are: " + str(user.income.keys()) + ": ")
                amount = float(input("Enter the amount in dollars: "))
                user.recordData(user.income, transactionType, amount)
    #Performing financial analysis
    