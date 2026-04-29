"""
-------------------------------------------------------
Personal Finance Tracker - Main Program
-------------------------------------------------------
Author: Butrus David Ngok
ID:     169142083
Email:  ngok2083@mylaurier.ca
__updated__ = "2026-04-28"
-------------------------------------------------------
"""

"""
-------------------------------------------------------
Personal Finance Tracker - Main
-------------------------------------------------------
Author: Butrus David Ngok
-------------------------------------------------------
"""

from functions import (
    get_float,
    get_expenses,
    calculate_total,
    calculate_savings,
    highest_expense,
    average_expense,
    save_to_file,
    display_file
)

print("=== Personal Finance Tracker ===")

# -----------------------------
# Input
# -----------------------------
income = get_float("Enter monthly income: ")

# -----------------------------
# Expenses
# -----------------------------
expenses = get_expenses()

# -----------------------------
# Process
# -----------------------------
total = calculate_total(expenses)
savings = calculate_savings(income, total)
highest = highest_expense(expenses)
average = average_expense(expenses)

# -----------------------------
# Output
# -----------------------------
print("\n--- Summary ---")
print(f"Total Expenses: ${total:.2f}")
print(f"Savings: ${savings:.2f}")
print(f"Highest Expense: ${highest:.2f}")
print(f"Average Expense: ${average:.2f}")

# -----------------------------
# Save
# -----------------------------
month = input("\nEnter month: ").strip()
if month == "":
    month = "Unknown"

save_to_file("finance.txt", month, income, expenses, total, savings)

# -----------------------------
# Display
# -----------------------------
choice = input("\nDisplay saved records? (y/n): ").strip().lower()

if choice == "y":
    display_file("finance.txt")

print("\nProgram finished.")