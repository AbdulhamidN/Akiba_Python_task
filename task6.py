employee = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport = float(input("Enter transport allowance: "))
food = float(input("Enter food allowance: "))

gross_salary = basic_salary + transport + food

print("========================================")
print("             EMPLOYEE PAYSLIP")
print("========================================")
print()
print("Employee:", employee)
print()
print("Basic Salary:", basic_salary, "ETB")
print("Transport Allowance:", transport, "ETB")
print("Food Allowance:", food, "ETB")
print("----------------------------------------")
print("Gross Salary:", gross_salary, "ETB")
print("========================================")