def get_valid_name():
    while True:
        name = input("Enter Employee Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Error: Name must contain alphabets only.")
        elif len(name) > 50:
            print("Error: Name must not exceed 50 characters.")
        else:
            return name


def get_valid_empid():
    while True:
        emp_id = input("Enter Employee ID: ").strip()
        if not emp_id.isalnum():
            print("Error: EmpID must be alphanumeric.")
        elif not (5 <= len(emp_id) <= 10):
            print("Error: EmpID length must be between 5 and 10 characters.")
        else:
            return emp_id


def get_valid_salary(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or (not allow_zero and value == 0):
                print("Error: Value must be positive.")
            elif value > 10000000:
                print("Error: Value must not exceed ₹1,00,00,000.")
            else:
                return value
        except ValueError:
            print("Error: Please enter numeric values only.")


def get_valid_bonus():
    while True:
        try:
            bonus = float(input("Enter Bonus Percentage (0–100): "))
            if bonus < 0 or bonus > 100:
                print("Error: Bonus percentage must be between 0 and 100.")
            else:
                return bonus
        except ValueError:
            print("Error: Please enter numeric values only.")


print("\nEnter Employee Details")

name = get_valid_name()
emp_id = get_valid_empid()
basic_salary = get_valid_salary("Enter Basic Monthly Salary: ", allow_zero=False)
special_allowances = get_valid_salary("Enter Special Allowances (Monthly): ")
bonus_percentage = get_valid_bonus()


gross_monthly_salary = basic_salary + special_allowances

if gross_monthly_salary <= 0:
    print("Error: Gross Monthly Salary must be greater than zero.")
    exit()

annual_gross_salary = gross_monthly_salary * 12
bonus_amount = annual_gross_salary * bonus_percentage / 100
annual_gross_salary += bonus_amount

if annual_gross_salary > 50000000:
    print("Error: Annual Gross Salary exceeds realistic limits.")
    exit()

print("\nAll inputs are valid ✔")
print("\nEmployee Summary")
print("-" * 40)
print(f"Name                  : {name}")
print(f"EmpID                 : {emp_id}")
print(f"Gross Monthly Salary  : ₹{gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary   : ₹{annual_gross_salary:,.2f}")
