0# Test Cases for Taxable Income Calculation Program

## Test Case 1: Annual gross salary greater than standard deduction
**Input:**
- Annual Gross Salary: 600000

**Expected Output:**
- Annual Gross Salary: ₹600000.00
- Standard Deduction: ₹50000.00
- Taxable Income: ₹550000.00

---

## Test Case 2: Annual gross salary equal to standard deduction
**Input:**
- Annual Gross Salary: 50000

**Expected Output:**
- Annual Gross Salary: ₹50000.00
- Standard Deduction: ₹50000.00
- Taxable Income: ₹0.00

---

## Test Case 3: Annual gross salary less than standard deduction
**Input:**
- Annual Gross Salary: 30000

**Expected Output:**
- Annual Gross Salary: ₹30000.00
- Standard Deduction: ₹50000.00
- Taxable Income: ₹0.00

---

## Test Case 4: Annual gross salary is zero
**Input:**
- Annual Gross Salary: 0

**Expected Output:**
- Annual Gross Salary: ₹0.00
- Standard Deduction: ₹50000.00
- Taxable Income: ₹0.00

---

## Test Case 5: Annual gross salary as decimal value
**Input:**
- Annual Gross Salary: 725000.75

**Expected Output:**
- Annual Gross Salary: ₹725000.75
- Standard Deduction: ₹50000.00
- Taxable Income: ₹675000.75

---

## Test Case 6: Very large annual gross salary
**Input:**
- Annual Gross Salary: 10000000

**Expected Output:**
- Annual Gross Salary: ₹10000000.00
- Standard Deduction: ₹50000.00
- Taxable Income: ₹9950000.00

---

## Test Case 7: Negative annual gross salary
**Input:**
- Annual Gross Salary: -450000

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for Annual Gross Salary

---

## Test Case 8: Non-numeric input (alphabetic)
**Input:**
- Annual Gross Salary: abc

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Annual Gross Salary

---

## Test Case 9: Non-numeric input (special characters)
**Input:**
- Annual Gross Salary: @@@

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Annual Gross Salary

---

## Test Case 10: Input with leading and trailing spaces
**Input:**
- Annual Gross Salary:   800000  

**Expected Output:**
- Annual Gross Salary: ₹800000.00
- Standard Deduction: ₹50000.00
- Taxable Income: ₹750000.00
