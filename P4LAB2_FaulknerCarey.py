# Carey Faulkner
# 03 APR 2025
# Multiplication Table Program with for and while loops

# Main loop to repeat the whole program
run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter an integer: "))

    if number < 0:
        print("This program does not handle negative numbers")
    else:
        print(f"\n{number}")
        print("\n")
        for i in range(1, 13):  # for loop to display table from 1 to 12
            print(f"{number} x {i} = {number * i}")

    print()  # Blank line for spacing
    run_again = input("Do you want to run the program again? (yes/no): ")

print("\nExiting program...")