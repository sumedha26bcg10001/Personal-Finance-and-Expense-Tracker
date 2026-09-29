from income import add_income, edit_income, delete_income, view_income
from expenses import add_expense, edit_expense, delete_expense, view_expenses

from analysis import calculate_total_income, calculate_total_expense
from reports import generate_report

from storage import load_data, save_data

from validation import get_valid_name, get_positive_number
from utils import calculate_balance, format_currency, print_separator


def main():

    print_separator()
    print("PERSONAL FINANCE TRACKER")
    print_separator()

    # Load previously saved data
    income_data, expense_data = load_data()

    month = get_valid_name("Enter month: ")

    while True:

        print("\n")
        print_separator()
        print("MAIN MENU")
        print_separator()

        print("1. Add Income")
        print("2. View Income")
        print("3. Edit Income")
        print("4. Delete Income")
        print("5. Add Expense")
        print("6. View Expenses")
        print("7. Edit Expense")
        print("8. Delete Expense")
        print("9. View Financial Summary")
        print("10. Generate Monthly Report")
        print("11. Save Data")
        print("12. Exit")

        print_separator()

        choice = input("Enter your choice (1-12): ")

        # --------------------------------
        # INCOME
        # --------------------------------

        if choice == "1":

            add_income(income_data)

            # Save automatically after adding
            save_data(income_data, expense_data)

        elif choice == "2":

            view_income(income_data)

        elif choice == "3":

            edit_income(income_data)

            # Save automatically after editing
            save_data(income_data, expense_data)

        elif choice == "4":

            delete_income(income_data)

            # Save automatically after deleting
            save_data(income_data, expense_data)

        # --------------------------------
        # EXPENSES
        # --------------------------------

        elif choice == "5":

            add_expense(expense_data)

            # Save automatically after adding
            save_data(income_data, expense_data)

        elif choice == "6":

            view_expenses(expense_data)

        elif choice == "7":

            edit_expense(expense_data)

            # Save automatically after editing
            save_data(income_data, expense_data)

        elif choice == "8":

            delete_expense(expense_data)

            # Save automatically after deleting
            save_data(income_data, expense_data)

        # --------------------------------
        # FINANCIAL SUMMARY
        # --------------------------------

        elif choice == "9":

            total_income = calculate_total_income(income_data)
            total_expense = calculate_total_expense(expense_data)
            balance = calculate_balance(income_data, expense_data)

            print("\n")
            print_separator()
            print("FINANCIAL SUMMARY")
            print_separator()

            print("Total Income :", format_currency(total_income))
            print("Total Expense:", format_currency(total_expense))
            print("Balance      :", format_currency(balance))

            print_separator()

            if balance > 0:
                print("You have money remaining this month.")

            elif balance == 0:
                print("Your income and expenses are equal.")

            else:
                print("Your expenses are greater than your income.")

        # --------------------------------
        # MONTHLY REPORT
        # --------------------------------

        elif choice == "10":

            generate_report(
                month,
                income_data,
                expense_data
            )

        # --------------------------------
        # MANUAL SAVE
        # --------------------------------

        elif choice == "11":

            save_data(
                income_data,
                expense_data
            )

        # --------------------------------
        # EXIT
        # --------------------------------

        elif choice == "12":

            # Save before exiting
            save_data(
                income_data,
                expense_data
            )

            print("\nYour data has been saved.")
            print("Thank you for using Personal Finance Tracker!")

            break

        else:

            print("\nInvalid choice.")
            print("Please enter a number between 1 and 12.")


# Start the program
if __name__ == "__main__":
    main()
