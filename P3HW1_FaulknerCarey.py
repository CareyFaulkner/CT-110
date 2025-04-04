# Carey Faulkner
# 03 APR 2025
# P3HW1
# This program takes a number grade, determines average, and displays letter grade for average.

# Enter grades for six modules
mod_1 = int(input("Enter grade for Module 1: "))
mod_2 = int(input("Enter grade for Module 2: "))
mod_3 = int(input("Enter grade for Module 3: "))
mod_4 = int(input("Enter grade for Module 4: "))
mod_5 = int(input("Enter grade for Module 5: "))
mod_6 = int(input("Enter grade for Module 6: "))

# Store grades in a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Calculate stats
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results
print('------Results------')
print(f"Lowest Grade:    {low}")
print(f"Highest Grade:   {high}")
print(f"Sum of Grades:   {total}")
print(f"Average:         {avg:.2f}")

# Determine letter grade
print('----Letter Grade----')
if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")
