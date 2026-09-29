def calculate_total_income(income_data):
    return sum(income_data.values())


def calculate_total_expense(expense_data):
    total_expense=0
    for expense in expense_data.values():
        total_expense += expense["amount"]
    return total_expense



def calculate_balance(income_data, expense_data):
    total_income = calculate_total_income(income_data)
    total_expense = calculate_total_expense(expense_data)

    balance = total_income - total_expense

    print("\n----------- FINANCIAL SUMMARY -----------")
    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Balance:", balance)

    return balance