"""
-------------------------------------------------------
Personal Finance Tracker - Functions
-------------------------------------------------------
Author: Butrus David Ngok
ID:     169142083
Email:  ngok2083@mylaurier.ca
__updated__ = "2026-04-28"
-------------------------------------------------------
"""

def get_float(prompt):
    """
    Safely gets a float input from the user.
    Prevents infinite loops by limiting retries.
    """
    attempts = 0

    while attempts < 5:
        user_input = input(prompt).strip()

        if user_input == "":
            print("Input cannot be empty.")
            attempts += 1
            continue

        try:
            value = float(user_input)

            if value < 0:
                print("Value cannot be negative.")
                attempts += 1
            else:
                return value

        except ValueError:
            print("Invalid input! Enter a number (e.g., 25.50)")
            attempts += 1

    print("Too many invalid attempts. Defaulting to 0.")
    return 0


def get_expenses():
    """
    Gets expense names and values from user.
    """
    expenses = {}

    print("\nEnter expenses (type 'done' to finish):")

    for _ in range(20):   # hard limit → NO infinite loop
        name = input("Expense name: ").strip()

        if name.lower() == "done":
            break

        if name == "":
            print("Name cannot be empty.")
            continue

        amount = get_float("Amount: ")
        expenses[name] = amount

    return expenses


def calculate_total(expenses):
    total = 0
    for value in expenses.values():
        total += value
    return total


def calculate_savings(income, total):
    return income - total


def highest_expense(expenses):
    if not expenses:
        return 0
    return max(expenses.values())


def average_expense(expenses):
    if not expenses:
        return 0
    return sum(expenses.values()) / len(expenses)


def save_to_file(filename, month, income, expenses, total, savings):
    """
    Saves formatted output like a table (NOT CSV)
    """
    with open(filename, "a") as fh:

        fh.write(f"\n===== {month.upper()} =====\n")
        fh.write(f"{'Item':<20}{'Amount ($)':>15}\n")
        fh.write("-" * 35 + "\n")

        for name, amount in expenses.items():
            fh.write(f"{name:<20}{amount:>15.2f}\n")

        fh.write("-" * 35 + "\n")
        fh.write(f"{'Total':<20}{total:>15.2f}\n")
        fh.write(f"{'Income':<20}{income:>15.2f}\n")
        fh.write(f"{'Savings':<20}{savings:>15.2f}\n")
        fh.write("=" * 35 + "\n")


def display_file(filename):
    """
    Displays saved file safely
    """
    try:
        with open(filename, "r") as fh:
            print("\n--- Saved Records ---\n")
            print(fh.read())
    except FileNotFoundError:
        print("No records found.")