# Carey Faulkner
# 03 APR 2025
# P3LAB
# This program calculates the most efficient way to represent a float amount
# using dollars, quarters, dimes, nickels, and pennies.

# Get input from the user
amount = float(input("Enter the amount of money as a float:"))

# Convert to cents
cents = int(round(amount * 100))

# Calculate each denomination
dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents 

# Function to print the correct word
def print_coin(count, singular, plural):
    if count == 1:
        print(f"{count} {singular}")
    elif count > 1:
        print(f"{count} {plural}")

# Output only the denominations that are used
if dollars: print_coin(dollars, "Dollar", "Dollars")
if quarters: print_coin(quarters, "Quarter", "Quarters")
if dimes: print_coin(dimes, "Dime", "Dimes")
if nickels: print_coin(nickels, "Nickel", "Nickels")
if pennies: print_coin(pennies, "Penny", "Pennies")