import json
from analysis import calculate_total_income, calculate_total_expense


def generate_report(month, income_data, expense_data):

    total_income = calculate_total_income(income_data)
    total_expense = calculate_total_expense(expense_data)

    balance = total_income - total_expense

    report = {
        "Month": month,
        "Income": income_data,
        "Total Income": total_income,
        "Expense": expense_data,
        "Total Expense": total_expense,
        "Balance": balance
    }

    print("\n----------- MONTHLY REPORT -----------")
    print(json.dumps(report, indent=6))

    return report