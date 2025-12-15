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

def calculate_tax(taxable_income):
    slabs = [
        (300000, 0.0),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]
    tax = 0.0
    prev_limit = 0
    for upper_limit, rate in slabs:
        if taxable_income > prev_limit:
            taxable_at_slab = min(taxable_income, upper_limit) - prev_limit
            tax += taxable_at_slab * rate
            prev_limit = upper_limit
        else:
            break
    return tax

print("Enter Employee Details:")
name = get_name_input("Name: ")
emp_id = input("EmpID: ").strip()
basic_salary = get_numeric_input("Basic Monthly Salary: ")
special_allowances = get_numeric_input("Special Allowances (Monthly): ")
bonus_percentage = get_numeric_input("Bonus Percentage (Annual % of Gross Salary): ")

gross_monthly_salary = basic_salary + special_allowances
annual_gross_salary = (gross_monthly_salary * 12) + (gross_monthly_salary * 12 * bonus_percentage / 100)

# Standard Deduction
standard_deduction = 50000
taxable_income = max(0, annual_gross_salary - standard_deduction)

# Tax Calculation
if taxable_income <= 700000:  # Section 87A rebate
    tax_before_cess = 0
else:
    tax_before_cess = calculate_tax(taxable_income)

cess = tax_before_cess * 0.04
total_tax = tax_before_cess + cess

annual_net_salary = annual_gross_salary - total_tax

# Display Report
print("\nEmployee Tax Report")
print(f"{'Field':<25}{'Details'}")
print(f"{'-'*40}")
print(f"{'Name':<25}{name}")
print(f"{'EmpID':<25}{emp_id}")
print(f"{'Gross Monthly Salary':<25}₹{gross_monthly_salary:,.2f}")
print(f"{'Annual Gross Salary':<25}₹{annual_gross_salary:,.2f}")
print(f"{'Taxable Income':<25}₹{taxable_income:,.2f}")
print(f"{'Tax Payable (before cess)':<25}₹{tax_before_cess:,.2f}")
print(f"{'Health & Education Cess (4%)':<25}₹{cess:,.2f}")
print(f"{'Total Tax Payable':<25}₹{total_tax:,.2f}")
print(f"{'Annual Net Salary':<25}₹{annual_net_salary:,.2f}")
