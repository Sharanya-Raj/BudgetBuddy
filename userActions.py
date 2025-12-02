from datetime import datetime, timedelta
from user import User 
import matplotlib.pyplot as myPlot

class userActions:
    def __init__(self, userName, password, email, studentNJIT, newAcct,help_category):
        self.userName = userName
        self.password = password
        self.email = email
        self.studentNJIT = studentNJIT
        self.newAcct = newAcct 
        self.user.recurringBills = []
        self.expenseType = ["Housing", "Utilities", "Groceries", "Dining Out", "Entertainment", "Transportation", "Miscellaneous"]
        self.revenueType = ["Salary", "Freelance Work", "Investment Gains", "Gifts", "Miscellaneous"]

    def transactionTracker(self, typeDict):
        '''Displays all transactions in the given dictionary (revenue/expense).'''
        for transaction in typeDict:
            print(transaction+": $"+str(typeDict[transaction]),end="\n")
        
        # If the dictionary is empty, then skip the plotting
        if len(typeDict) == 0:
            print("No data for graph.")
            return 
        
        plotLabels = list(typeDict.keys())
        plotValues = list(typeDict.values())

        myPlot.figure(figsize=(7,4))
        myPlot.bar(plotLabels, plotValues)
        myPlot.title("Transaction Overview")
        myPlot.xlabel("Category")
        myPlot.yLabel("Amount ($)")
        myPlot.xticks(rotation = 45)
        myPlot.tight_layout()
        myPlot.show()

    def recordData(self, typeDict, transactionType, amount):
        '''Records a new transaction by updating the appropriate dictionary.'''
        if transactionType in typeDict:
            typeDict[transactionType] += amount
        else:
            typeDict[transactionType] = amount

    def totalCalculator(self, typeDict):
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
    
        
    def budgetAdvisor(self, income, expenses):
        '''Provides budget advice based on income and expenses.'''
        if expenses > income:
            return "Your expenses exceed your income. Consider reducing non-essential spending."
        elif expenses == income:
            return "Your expenses match your income. Try to save a portion of your income."
        else:
            return "Great job! Your income exceeds your expenses. Consider investing or saving the surplus."
    
    def recurringAlerts(self):
        """Check bills in self.user.recurringBills and alert if due within 3 days"""
        today = datetime.today().date()
        alert_threshold = today + timedelta(days=3)
        if len(self.user.recurringBills) == 0:
            print("No recurring bills found.")
            return

        for bill in self.user.recurringBills:
            bill_name= bill[0]
            amount = bill[1]
            due_date_str = bill[2]
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            if today <= due_date and due_date <= alert_threshold:
                print(f"Alert: '{bill_name}' of ${amount:.2f} is due on {due_date}")

    def addRecurringBill(self, bill_name, amount, due_date):
        """Add a new recurring bill to self.user.recurringBills"""
        self.user.recurringBills.append([bill_name, amount, due_date])

    def removeRecurringBill(self, bill_name):
        """Remove a recurring bill from self.user.recurringBills by name"""
        for bill in self.user.recurringBills:
            if bill[0] == bill_name:
                self.user.recurringBills.remove(bill)
                print(f"Removed recurring bill: {bill_name}")
                return
        print(f"No recurring bill found with the name: {bill_name}")
    

        
