# Carey Faulkner
# 03 APR 2025
# P3HW2
# This program calculates employee pay including overtime

# Pseudocode:
# 1. Ask the user to enter the employee's name.
# 2. Ask the user to enter the number of hours worked.
# 3. Ask the user to enter the pay rate.
# 4. If hours worked is more than 40:
#       Calculate overtime hours.
#       Calculate overtime pay at 1.5x pay rate.
#       Calculate regular pay for 40 hours.
# 5. Else:
#       No overtime hours.
#       Regular pay is hours times pay rate.
# 6. Calculate gross pay as regular pay plus overtime pay.
# 7. Display:
#       Employee name
#       Pay rate
#       Hours worked
#       Overtime hours
#       Overtime pay
#       Regular pay
#       Gross pay

# Input
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculations
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

print("\n---------------------------------------------------------------------------------------------")
print(f"Employee Name:     {employee_name}\n")

# Output Header
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<17}"
      f"{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("---------------------------------------------------------------------------------------------")

# Output Data Row
print(f"{hours_worked:<15.2f}${pay_rate:<11.2f}{overtime_hours:<17.2f}"
      f"${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<.2f}")