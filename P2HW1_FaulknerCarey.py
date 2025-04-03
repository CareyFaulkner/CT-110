# Carey Faulkner
# 16 MAR 2025
# P2HW1
# Take travel destinations and costs and format cleaner results.

print('This program calculates and displays travel expenses\n\n')
budget = float(input('Enter budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think you spend on gas: '))
print()
accomodations = int(input('Approximately, how much will you need for accomodations/hotel: '))
print()
food = float(input('Last, how much will you need for food: '))
print()
print("\n----- Travel Expenses -----\n")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas:,.2f}")
print(f"{'Accommodations:':<20} ${accomodations:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}\n")
print("----------------------------------")
expenses = gas + accomodations + food
remaining_budget = budget - expenses
print(f"{'Remaining Balance:':<20} ${remaining_budget:,.2f}")
