import unittest

from income import add_income
from expenses import add_expense
from analysis import calculate_total_income
from analysis import calculate_total_expense
from analysis import calculate_balance


class TestFinanceTracker(unittest.TestCase):

    def test_total_income(self):
        income_data = {
            "Salary": 30000,
            "Freelance": 5000
        }

        total = calculate_total_income(income_data)

        self.assertEqual(total, 35000)

    def test_total_expense(self):
        expense_data = {
            "Food": {
                "description": "Groceries",
                "amount": 3000
            },
            "Transport": {
                "description": "Fuel",
                "amount": 2000
            }
        }

        total = calculate_total_expense(expense_data)

        self.assertEqual(total, 5000)

    def test_balance(self):
        income_data = {
            "Salary": 30000
        }

        expense_data = {
            "Food": {
                "description": "Groceries",
                "amount": 5000
            }
        }

        balance = calculate_balance(
            income_data,
            expense_data
        )

        self.assertEqual(balance, 25000)

    def test_empty_income(self):
        income_data = {}

        total = calculate_total_income(income_data)

        self.assertEqual(total, 0)

    def test_empty_expense(self):
        expense_data = {}

        total = calculate_total_expense(expense_data)

        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()