def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_name_input(prompt):
    while True:
        name = input(prompt).strip()
        if all(x.isalpha() or x.isspace() for x in name) and name != "":
            return name
        else:
            print("Invalid input! Name should contain alphabets only.")

def main():
    print("Enter Employee Details:")
    name = get_name_input("Name: ")
    emp_id = input("EmpID: ").strip()
    basic_salary = get_numeric_input("Basic Monthly Salary: ")
    special_allowances = get_numeric_input("Special Allowances (Monthly): ")
    bonus_percentage = get_numeric_input("Bonus Percentage (Annual % of Gross Salary): ")

    gross_monthly_salary = basic_salary + special_allowances
    annual_gross_salary = (gross_monthly_salary * 12) + (gross_monthly_salary * 12 * bonus_percentage / 100)

    print("\nEmployee Salary Details:")
    print(f"Name: {name}")
    print(f"EmpID: {emp_id}")
    print(f"Gross Monthly Salary: ₹{gross_monthly_salary:.2f}")
    print(f"Annual Gross Salary (including bonus): ₹{annual_gross_salary:.2f}")

main()
