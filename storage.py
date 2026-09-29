import json
import os


DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "finance.json")


def save_data(income_data, expense_data):
    """Save income and expense data to the JSON file."""

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    data = {
        "income": income_data,
        "expenses": expense_data
    }

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("Financial data saved successfully.")

    except Exception as e:
        print("Error saving data:", e)


def load_data():
    """Load income and expense data from the JSON file."""

    if not os.path.exists(DATA_FILE):
        return {}, {}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        income_data = data.get("income", {})
        expense_data = data.get("expenses", {})

        return income_data, expense_data

    except (json.JSONDecodeError, FileNotFoundError):
        print("Could not load saved data.")
        return {}, {}