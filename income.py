def add_income(income_data):
    try:
        num_source = int(input("Enter number of sources of income: "))

        for i in range(num_source):
            source = input("Enter source of income: ")
            income = float(input("Enter income from this source: "))

            income_data[source] = income

        print("Income added successfully.")

    except ValueError:
        print("Please enter a valid number.")


def view_income(income_data):
    print("\nIncome Data:")

    if not income_data:
        print("No income recorded.")
        return

    total_income = sum(income_data.values())

    for source, amount in income_data.items():
        print(source, ":", amount)

    print("Total Income:", total_income)


def edit_income(income_data):
    if not income_data:
        print("No income available to edit.")
        return

    source = input("Enter the source whose income needs to be edited: ")

    if source in income_data:
        try:
            new_income = float(input("Enter edited income : "))
            income_data[source] = new_income
            print("Income updated successfully.")
            total_income = sum(income_data.values())
        except ValueError:
            print("Please enter a valid amount.")
    else:
        print("Income source not found.")


def delete_income(income_data):
    if not income_data:
        print("No income available to delete.")
        return

    source = input("Enter income source that needs to be deleted: ")

    if source in income_data:
        del income_data[source]
        print("Income deleted successfully.")
    else:
        print("Income source not found.")