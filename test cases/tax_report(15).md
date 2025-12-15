# Test Cases for Employee Salary & Tax Calculation System

---

## Test Case 1: Valid inputs – taxable income below 87A rebate limit
**Input:**
- Name: Ananya
- EmpID: EMP001
- Basic Monthly Salary: 40000
- Special Allowances: 10000
- Bonus Percentage: 0

**Expected Output:**
- Gross Monthly Salary: ₹50000.00
- Annual Gross Salary: ₹600000.00
- Taxable Income: ₹550000.00
- Total Tax Payable: ₹0.00
- Annual Net Salary: ₹600000.00

---

## Test Case 2: Taxable income exactly at 87A rebate limit
**Input:**
- Name: Rahul
- EmpID: EMP002
- Basic Monthly Salary: 50000
- Special Allowances: 10000
- Bonus Percentage: 0

**Expected Output:**
- Annual Gross Salary: ₹720000.00
- Taxable Income: ₹670000.00
- Total Tax Payable: ₹0.00
- Annual Net Salary: ₹720000.00

---

## Test Case 3: Taxable income just above rebate limit
**Input:**
- Name: Sneha
- EmpID: EMP003
- Basic Monthly Salary: 52000
- Special Allowances: 10000
- Bonus Percentage: 0

**Expected Output:**
- Taxable Income: ₹694000.00
- Total Tax Payable: ₹0.00
- Annual Net Salary: ₹744000.00

---

## Test Case 4: Taxable income in 10% slab
**Input:**
- Name: Ramesh
- EmpID: EMP004
- Basic Monthly Salary: 70000
- Special Allowances: 10000
- Bonus Percentage: 0

**Expected Output:**
- Taxable Income: ₹910000.00
- Tax Payable (before cess): ₹30000.00
- Total Tax Payable: ₹31200.00
- Annual Net Salary: ₹948800.00

---

## Test Case 5: Taxable income in 15% slab
**Input:**
- Name: Kiran
- EmpID: EMP005
- Basic Monthly Salary: 95000
- Special Allowances: 10000
- Bonus Percentage: 0

**Expected Output:**
- Taxable Income: ₹1130000.00
- Total Tax Payable: ₹62400.00
- Annual Net Salary: ₹1197600.00

---

## Test Case 6: Taxable income in 20% slab
**Input:**
- Name: Meena
- EmpID: EMP006
- Basic Monthly Salary: 120000
- Special Allowances: 10000
- Bonus Percentage: 0

**Expected Output:**
- Taxable Income: ₹1510000.00
- Total Tax Payable: ₹109200.00
- Annual Net Salary: ₹1570800.00

---

## Test Case 7: Taxable income above highest slab
**Input:**
- Name: Arjun
- EmpID: EMP007
- Basic Monthly Salary: 200000
- Special Allowances: 50000
- Bonus Percentage: 10

**Expected Output:**
- Taxable Income: ₹3350000.00
- Total Tax Payable: ₹1009200.00
- Annual Net Salary: ₹2990800.00

---

## Test Case 8: Bonus percentage applied
**Input:**
- Name: Pooja
- EmpID: EMP008
- Basic Monthly Salary: 60000
- Special Allowances: 5000
- Bonus Percentage: 10

**Expected Output:**
- Annual Gross Salary: ₹858000.00
- Taxable Income: ₹808000.00
- Total Tax Payable: ₹26000.00
- Annual Net Salary: ₹832000.00

---

## Test Case 9: Zero salaries
**Input:**
- Name: Kavya
- EmpID: EMP009
- Basic Monthly Salary: 0
- Special Allowances: 0
- Bonus Percentage: 0

**Expected Output:**
- Annual Gross Salary: ₹0.00
- Taxable Income: ₹0.00
- Annual Net Salary: ₹0.00

---

## Test Case 10: Decimal salary values
**Input:**
- Name: Suresh
- EmpID: EMP010
- Basic Monthly Salary: 45500.75
- Special Allowances: 3499.25
- Bonus Percentage: 5.5

**Expected Output:**
- Gross Monthly Salary: ₹49000.00
- Annual Gross Salary: ₹620940.00
- Taxable Income: ₹570940.00
- Total Tax Payable: ₹0.00
- Annual Net Salary: ₹620940.00

---

## Test Case 11: Invalid name (numbers)
**Input:**
- Name: Ananya123

**Expected Output:**
- Invalid input! Name should contain alphabets only.
- Prompt repeats for Name

---

## Test Case 12: Invalid name (special characters)
**Input:**
- Name: Rahul@#

**Expected Output:**
- Invalid input! Name should contain alphabets only.
- Prompt repeats for Name

---

## Test Case 13: Empty name
**Input:**
- Name: (empty)

**Expected Output:**
- Invalid input! Name should contain alphabets only.
- Prompt repeats for Name

---

## Test Case 14: Negative salary input
**Input:**
- Basic Monthly Salary: -40000

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for salary

---

## Test Case 15: Non-numeric salary input
**Input:**
- Special Allowances: abc

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for allowances

---

## Test Case 16: Negative bonus percentage
**Input:**
- Bonus Percentage: -10

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for bonus percentage

---

## Test Case 17: Very large salary values
**Input:**
- Name: Rohit
- EmpID: EMP011
- Basic Monthly Salary: 1000000
- Special Allowances: 500000
- Bonus Percentage: 20

**Expected Output:**
- Annual Gross Salary: ₹21600000.00
- Total Tax Payable: ₹2262000.00
- Annual Net Salary: ₹19338000.00
