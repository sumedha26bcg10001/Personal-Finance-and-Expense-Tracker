def is_positive_number(value):
    """Check whether a value is a positive number."""

    try:
        number = float(value)

        if number > 0:
            return True

        return False

    except ValueError:
        return False


def is_non_negative_number(value):
    """Check whether a value is zero or a positive number."""

    try:
        number = float(value)

        if number >= 0:
            return True

        return False

    except ValueError:
        return False


def is_valid_name(name):
    """Check whether a name is not empty."""

    if name.strip() == "":
        return False

    return True


def get_positive_number(prompt):
    """Keep asking until the user enters a positive number."""

    while True:
        value = input(prompt)

        if is_positive_number(value):
            return float(value)

        print("Please enter a positive number.")


def get_valid_name(prompt):
    """Keep asking until the user enters a valid name."""

    while True:
        name = input(prompt)

        if is_valid_name(name):
            return name.strip()

        print("Name cannot be empty.")