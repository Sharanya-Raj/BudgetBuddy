def evaluatespending(amount, income):
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






