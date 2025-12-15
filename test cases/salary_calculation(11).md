# Test Cases for Employee Salary Calculation Program

## Test Case 1: Valid inputs (normal case)
**Input:**
- Name: Ananya
- EmpID: EMP001
- Basic Monthly Salary: 30000
- Special Allowances (Monthly): 5000
- Bonus Percentage: 10

**Expected Output:**
- Gross Monthly Salary: ₹35000.00
- Annual Gross Salary: ₹462000.00

---

## Test Case 2: Valid inputs with zero bonus
**Input:**
- Name: Rahul
- EmpID: EMP002
- Basic Monthly Salary: 40000
- Special Allowances (Monthly): 10000
- Bonus Percentage: 0

**Expected Output:**
- Gross Monthly Salary: ₹50000.00
- Annual Gross Salary: ₹600000.00

---

## Test Case 3: Valid inputs with zero special allowances
**Input:**
- Name: Sneha
- EmpID: EMP003
- Basic Monthly Salary: 45000
- Special Allowances (Monthly): 0
- Bonus Percentage: 5

**Expected Output:**
- Gross Monthly Salary: ₹45000.00
- Annual Gross Salary: ₹567000.00

---

## Test Case 4: Valid inputs with decimal values
**Input:**
- Name: Pooja
- EmpID: EMP004
- Basic Monthly Salary: 32500.75
- Special Allowances (Monthly): 2499.25
- Bonus Percentage: 7.5

**Expected Output:**
- Gross Monthly Salary: ₹35000.00
- Annual Gross Salary: ₹451500.00

---

## Test Case 5: Bonus percentage greater than 100
**Input:**
- Name: Kiran
- EmpID: EMP005
- Basic Monthly Salary: 30000
- Special Allowances (Monthly): 5000
- Bonus Percentage: 150

**Expected Output:**
- Gross Monthly Salary: ₹35000.00
- Annual Gross Salary: ₹1050000.00

---

## Test Case 6: Name with spaces (valid)
**Input:**
- Name: Ananya Ingale
- EmpID: EMP006
- Basic Monthly Salary: 28000
- Special Allowances (Monthly): 7000
- Bonus Percentage: 10

**Expected Output:**
- Gross Monthly Salary: ₹35000.00
- Annual Gross Salary: ₹462000.00

---

## Test Case 7: Empty name (invalid)
**Input:**
- Name: (empty)

**Expected Output:**
- Invalid input! Name should contain alphabets only.
- Prompt repeats for Name

---

## Test Case 8: Name with numbers
**Input:**
- Name: Ananya123

**Expected Output:**
- Invalid input! Name should contain alphabets only.
- Prompt repeats for Name

---

## Test Case 9: Name with special characters
**Input:**
- Name: Rahul@#

**Expected Output:**
- Invalid input! Name should contain alphabets only.
- Prompt repeats for Name

---

## Test Case 10: Negative basic salary
**Input:**
- Name: Meena
- EmpID: EMP007
- Basic Monthly Salary: -25000

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for Basic Monthly Salary

---

## Test Case 11: Negative special allowances
**Input:**
- Name: Ramesh
- EmpID: EMP008
- Basic Monthly Salary: 30000
- Special Allowances (Monthly): -5000

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for Special Allowances

---

## Test Case 12: Negative bonus percentage
**Input:**
- Name: Nisha
- EmpID: EMP009
- Basic Monthly Salary: 30000
- Special Allowances (Monthly): 5000
- Bonus Percentage: -10

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for Bonus Percentage

---

## Test Case 13: Non-numeric basic salary
**Input:**
- Name: Arjun
- EmpID: EMP010
- Basic Monthly Salary: abc

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Basic Monthly Salary

---

## Test Case 14: Non-numeric special allowances
**Input:**
- Name: Divya
- EmpID: EMP011
- Basic Monthly Salary: 30000
- Special Allowances (Monthly): @@@

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Special Allowances

---

## Test Case 15: Non-numeric bonus percentage
**Input:**
- Name: Suresh
- EmpID: EMP012
- Basic Monthly Salary: 30000
- Special Allowances (Monthly): 5000
- Bonus Percentage: xyz

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Bonus Percentage

---

## Test Case 16: All numeric inputs as zero
**Input:**
- Name: Kavya
- EmpID: EMP013
- Basic Monthly Salary: 0
- Special Allowances (Monthly): 0
- Bonus Percentage: 0

**Expected Output:**
- Gross Monthly Salary: ₹0.00
- Annual Gross Salary: ₹0.00

---

## Test Case 17: Very large salary values
**Input:**
- Name: Rohit
- EmpID: EMP014
- Basic Monthly Salary: 1000000
- Special Allowances (Monthly): 500000
- Bonus Percentage: 20

**Expected Output:**
- Gross Monthly Salary: ₹1500000.00
- Annual Gross Salary: ₹21600000.00

