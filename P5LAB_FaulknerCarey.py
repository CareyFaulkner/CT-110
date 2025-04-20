# Carey Faulkner
# 20 APR 2025
# P5LAB
# This program will simulate a customer using a self-checkout machine.

import random

# Function to break down and print change
def disperse_change(change):
    print("\nChange is: ${:.2f}".format(change))

    # Convert to cents to avoid float precision issues
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    # Output only coins that are used
    if dollars: print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters: print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes: print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels: print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies: print(f"{pennies} Penn{'ies' if pennies != 1 else 'y'}")


# Main logic
def main():
    # Generate total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${total_owed:.2f}")

    # Get user payment
    user_payment = float(input("How much cash will you put in the self-checkout: $"))

    # Validate payment
    while user_payment < total_owed:
        print("Insufficient funds. Please insert more money.")
        user_payment = float(input("How much cash will you put in the self-checkout: $"))

    # Calculate change
    change = round(user_payment - total_owed, 2)

    # Call function to disperse change
    disperse_change(change)


# Run program
main()
