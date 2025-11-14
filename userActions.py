from user import User 

class userActions:
    def __init__(self, user):
        self.user = user    
    def transactionTracker(self): 
        pass
    def recordData(dollarlst):
        pass
    def initializeUser(user):
        pass
    def loginUser(user):
        pass
    def totalCalculator(self):
        pass
    def connect_with_NJIT_resources(help_category):
        if help_category == "FINANCIAL_AID":
            return "Contact the Office of Student Financial Aid Services (SFAS) for FAFSA, grants, loans, scholarships, and special circumstances appeals."
        elif help_category == "BILLING_PAYMENTS":
            return "Contact the Office of the Bursar for your eStatement, payment plans, account holds, and tuition refunds."
        elif help_category == "EMERGENCY_FINANCE":
            return "Apply for the Highlander Student Emergency Fund through the Student Financial Aid Services Office for immediate, unexpected financial hardship."
        else:
            return "Please specify if your question is about FINANCIAL_AID, BILLING_PAYMENTS, or EMERGENCY_FINANCE to connect you with the right resource."
    def evaluatespending(self, amount, income):
        """
        Evaluates if the spending amount exceeds a given threshold.

        Parameters:
        amount (float): The spending amount to evaluate.
        threshold (float): The threshold to compare against.

        Returns:
        str: A message indicating whether the spending is within the limit or exceeds it.
        """
        if amount > income:
            return "Spending exceeds limit.You need to cut down your expenses."
        else:
            return "Spending is within the limit. You are doing good."