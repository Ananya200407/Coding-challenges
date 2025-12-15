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
    previous_limit = 0

    for upper_limit, rate in slabs:
        if taxable_income > previous_limit:
            taxable_at_slab = min(taxable_income, upper_limit) - previous_limit
            tax += taxable_at_slab * rate
            previous_limit = upper_limit
        else:
            break
    return tax

def main():
    # Input taxable income
    taxable_income = get_numeric_input("Enter Taxable Income (₹): ")

    # Section 87A Rebate
    if taxable_income <= 700000:
        tax_before_cess = 0
        rebate_applied = True
    else:
        tax_before_cess = calculate_tax(taxable_income)
        rebate_applied = False

    cess = tax_before_cess * 0.04
    total_tax = tax_before_cess + cess

    print("\nTax Breakdown:")
    print(f"Taxable Income: ₹{taxable_income:.2f}")
    if rebate_applied:
        print("Section 87A Rebate Applied: 100%")
        print("Tax before Cess: ₹0.00")
    else:
        print(f"Tax before Cess: ₹{tax_before_cess:.2f}")
    print(f"Health & Education Cess (4%): ₹{cess:.2f}")
    print(f"Total Tax Payable: ₹{total_tax:.2f}")

main()
