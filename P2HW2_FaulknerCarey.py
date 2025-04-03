# Carey Faulkner
# 03 APR 2025
# P2HW2
# This program calculates the average based on Module scores.

# Ask the user to enter grades for each module
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store the grades in a list
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculate the values
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Display the results
print('------Results------')
print(f"Lowest Grade:   {lowest}")
print(f"Highest Grade:  {highest}")
print(f"Sum of Grades:  {total}")
print(f"Average:        {average:.2f}")