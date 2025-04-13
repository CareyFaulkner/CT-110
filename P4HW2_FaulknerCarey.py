# Carey Faulkner
# 13 April 2025
# P4HW2
# Payroll Calculator with Totals and "Done" Feature

# Initialize totals
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

# Start sentinel loop
while True:
    employee_name = input("Enter employee name or 'Done' to finish: ")

    if employee_name.lower() == "done":
        break

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

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Output formatting
    print("\n---------------------------------------------------------------------------------------------")
    print(f"Employee Name:     {employee_name}\n")

    # Output Header
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<17}"
          f"{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("---------------------------------------------------------------------------------------------")

    # Output Data Row
    print(f"{hours_worked:<15.2f}${pay_rate:<11.2f}{overtime_hours:<17.2f}"
          f"${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<.2f}\n")

# Final Summary Output
print("==============================================")
print("              PAYROLL SUMMARY                 ")
print("==============================================")
print(f"Total Employees Entered: {employee_count}")
print(f"Total Overtime Pay:      ${total_overtime_pay:.2f}")
print(f"Total Regular Pay:       ${total_regular_pay:.2f}")
print(f"Total Gross Pay:         ${total_gross_pay:.2f}")
print("==============================================")