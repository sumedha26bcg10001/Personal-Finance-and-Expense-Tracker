def add_expense(expense_data):
    try:
        num_expense = int(input("Enter number of expenses: "))

        for i in range(num_expense):
            category = input("Expense Category: ")
            description = input("Describe the reason to spend: ")
            amount = float(input("Enter amount spent: "))

            expense_data[category] = {
                "amount": amount,
                "description": description
            }

        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(expense_data):
    print("\nExpense Data:")

    if not expense_data:
        print("No expenses recorded.")
        return

    total_expense = 0

    for category in expense_data:
        amount=expense_data[category]["amount"]
        description=expense_data[category]["description"]
        print(
            category,
            ":",
            amount,
            "-",
            description
        )
        total_expense += amount

    print("Total Expense:", total_expense)


def edit_expense(expense_data):
    if not expense_data:
        print("No expenses available to edit.")
        return

    category = input("Enter expense category to edit: ")

    if category in expense_data:
        try:
            new_amount = float(input("Enter edited amount: "))
            expense_data[category]["amount"] = new_amount

            print("Expense updated successfully.")

        except ValueError:
            print("Please enter a valid amount.")

    else:
        print("Expense category not found.")


def delete_expense(expense_data):
    if not expense_data:
        print("No expenses available to edit.")
        return

    category = input("Enter expense category to edit: ")

    if category in expense_data:
        try:
            new_amount = float(input("Enter edited amount: "))
            expense_data[category]["amount"] = new_amount

            print("Expense updated successfully.")

        except ValueError:
            print("Please enter a valid amount.")

    else:
        print("Expense category not found.")


def delete_expense(expense_data):
    if not expense_data:
        print("No expenses available to delete.")
        return

    category = input("Enter expense category to delete: ")

    if category in expense_data:
        del expense_data[category]
        print("Expense deleted successfully.")

    else:
        print("Expense category not found.")