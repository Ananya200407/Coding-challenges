# Test Cases for Net Salary Calculation Program

## Test Case 1: Taxable income below Section 87A rebate limit
**Input:**
- Annual Gross Salary: 600000
- Taxable Income: 500000

**Expected Output:**
- Total Tax Payable: ₹0.00
- Annual Net Salary: ₹600000.00

---

## Test Case 2: Taxable income exactly at rebate limit (700000)
**Input:**
- Annual Gross Salary: 800000
- Taxable Income: 700000

**Expected Output:**
- Total Tax Payable: ₹0.00
- Annual Net Salary: ₹800000.00

---

## Test Case 3: Taxable income just above rebate limit
**Input:**
- Annual Gross Salary: 900000
- Taxable Income: 700001

**Expected Output:**
- Total Tax Payable: ₹20800.05
- Annual Net Salary: ₹879199.95

---

## Test Case 4: Taxable income in 10% slab
**Input:**
- Annual Gross Salary: 1000000
- Taxable Income: 900000

**Expected Output:**
- Total Tax Payable: ₹31200.00
- Annual Net Salary: ₹968800.00

---

## Test Case 5: Taxable income in 15% slab
**Input:**
- Annual Gross Salary: 1300000
- Taxable Income: 1200000

**Expected Output:**
- Total Tax Payable: ₹62400.00
- Annual Net Salary: ₹1237600.00

---

## Test Case 6: Taxable income in 20% slab
**Input:**
- Annual Gross Salary: 1600000
- Taxable Income: 1500000

**Expected Output:**
- Total Tax Payable: ₹109200.00
- Annual Net Salary: ₹1490800.00

---

## Test Case 7: Taxable income above highest slab
**Input:**
- Annual Gross Salary: 2200000
- Taxable Income: 2000000

**Expected Output:**
- Total Tax Payable: ₹265200.00
- Annual Net Salary: ₹1934800.00

---

## Test Case 8: Annual gross salary equals taxable income
**Input:**
- Annual Gross Salary: 750000
- Taxable Income: 750000

**Expected Output:**
- Total Tax Payable: ₹26000.00
- Annual Net Salary: ₹724000.00

---

## Test Case 9: Decimal values for salary and taxable income
**Input:**
- Annual Gross Salary: 1250000.75
- Taxable Income: 845000.50

**Expected Output:**
- Total Tax Payable: ₹25480.05
- Annual Net Salary: ₹1224520.70

---

## Test Case 10: Very large income values
**Input:**
- Annual Gross Salary: 10000000
- Taxable Income: 10000000

**Expected Output:**
- Total Tax Payable: ₹2262000.00
- Annual Net Salary: ₹7738000.00

---

## Test Case 11: Annual gross salary is zero
**Input:**
- Annual Gross Salary: 0
- Taxable Income: 0

**Expected Output:**
- Total Tax Payable: ₹0.00
- Annual Net Salary: ₹0.00

---

## Test Case 12: Negative annual gross salary
**Input:**
- Annual Gross Salary: -500000

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for Annual Gross Salary

---

## Test Case 13: Negative taxable income
**Input:**
- Annual Gross Salary: 800000
- Taxable Income: -200000

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for Taxable Income

---

## Test Case 14: Non-numeric annual gross salary
**Input:**
- Annual Gross Salary: abc

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Annual Gross Salary

---

## Test Case 15: Non-numeric taxable income
**Input:**
- Annual Gross Salary: 900000
- Taxable Income: xyz

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Taxable Income

---

## Test Case 16: Input with leading and trailing spaces
**Input:**
- Annual Gross Salary:   1000000  
- Taxable Income:   800000  

**Expected Output:**
- Total Tax Payable: ₹26000.00
- Annual Net Salary: ₹974000.00
