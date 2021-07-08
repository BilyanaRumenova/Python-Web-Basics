def calculate_budget_left(profile, expenses):
    total_expenses = sum(expense.price for expense in expenses)
    return profile.budget - total_expenses
