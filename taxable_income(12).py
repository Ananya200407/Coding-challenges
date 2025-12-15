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


annual_gross_salary = get_numeric_input("Enter Annual Gross Salary (₹): ")

standard_deduction = 50000

taxable_income = annual_gross_salary - standard_deduction
if taxable_income < 0:
    taxable_income = 0  

print("\nTaxable Income Calculation:")
print(f"Annual Gross Salary: ₹{annual_gross_salary:.2f}")
print(f"Standard Deduction: ₹{standard_deduction:.2f}")
print(f"Taxable Income: ₹{taxable_income:.2f}")
