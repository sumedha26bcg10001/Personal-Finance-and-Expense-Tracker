import unittest

from analysis import (
    calculate_total_income,
    calculate_total_expense,
    calculate_balance
)

from storage import save_data, load_data


class TestFinanceTracker(unittest.TestCase):

    # Test total income calculation
    def test_total_income(self):

        income_data = {
            "Salary": 500000,
            "Freelance": 1000
        }

        result = calculate_total_income(income_data)

        self.assertEqual(result, 501000)

    # Test total expense calculation
    def test_total_expense(self):

        expense_data = {
            "Food": {
                "description": "Vegetales and Fruits",
                "amount": 5000
            },
            "Transport": {
                "description": "Train and Cab",
                "amount": 1200
            }
        }

        result = calculate_total_expense(expense_data)

        self.assertEqual(result, 6200)

    # Test balance calculation
    def test_balance(self):

        income_data = {
            "Salary": 500000
        }

        expense_data = {
            "Food": {
                "description": "Vegetables and Fruits",
                "amount": 5000
            }
        }

        result = calculate_balance(
            income_data,
            expense_data
        )

        self.assertEqual(result, 494800)

    # Test empty income
    def test_empty_income(self):

        income_data = {}

        result = calculate_total_income(income_data)

        self.assertEqual(result, 0)

    # Test empty expenses
    def test_empty_expenses(self):

        expense_data = {}

        result = calculate_total_expense(expense_data)

        self.assertEqual(result, 0)

    # Test saving and loading data
    def test_storage(self):

        income_data = {
            "Salary": 500000
        }

        expense_data = {
            "Food": {
                "description": "Vegetables and Fruits",
                "amount": 5000
            }
        }

        save_data(income_data, expense_data)

        loaded_income, loaded_expenses = load_data()

        self.assertEqual(loaded_income, income_data)
        self.assertEqual(loaded_expenses, expense_data)


if __name__ == "__main__":
    unittest.main()
