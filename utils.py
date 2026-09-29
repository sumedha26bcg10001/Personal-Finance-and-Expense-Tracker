def calculate_total_income(income_data):
    """Calculate total income."""

    total = 0

    for amount in income_data.values():
        total += amount

    return total


def calculate_total_expense(expense_data):
    """Calculate total expenses."""

    total = 0

    for expense in expense_data.values():
        total += expense["amount"]

    return total


def calculate_balance(income_data, expense_data):
    """Calculate remaining balance."""

    total_income = calculate_total_income(income_data)
    total_expense = calculate_total_expense(expense_data)

    return total_income - total_expense


def format_currency(amount):
    """Format an amount as currency."""

    return f"₹{amount:,.2f}"


def print_separator():
    """Print a separator line."""

    print("-" * 45)