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

# Input Annual Gross Salary
annual_gross_salary = get_numeric_input("Enter Annual Gross Salary (₹): ")

taxable_income = get_numeric_input("Enter Taxable Income (₹): ")

if taxable_income <= 700000:  # Section 87A rebate
    tax_before_cess = 0
else:
    tax_before_cess = calculate_tax(taxable_income)

cess = tax_before_cess * 0.04
total_tax = tax_before_cess + cess

net_salary = annual_gross_salary - total_tax

print("\nNet Salary Calculation:")
print(f"Annual Gross Salary: ₹{annual_gross_salary:.2f}")
print(f"Total Tax Payable (including cess): ₹{total_tax:.2f}")
print(f"Annual Net Salary: ₹{net_salary:.2f}")
