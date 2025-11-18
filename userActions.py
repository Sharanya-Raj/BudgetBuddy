from user import User 

class userActions:
    def __init__(self, userName, password, email, studentNJIT, newAcct):
        self.user = User(userName, password, email, studentNJIT, newAcct)

    def transactionTracker(self, typeDict):
        '''Takes either revenue or expense transactions and displays them by type.'''
        for transaction in typeDict:
            print(transaction+": $"+str(typeDict[transaction]),end="\n")

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
    
    