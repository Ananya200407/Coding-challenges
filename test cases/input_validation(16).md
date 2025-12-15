# Test Cases for Employee Input Validation & Salary Calculation Program

---

## Test Case 1: All valid inputs (normal case)
**Input:**
- Name: Ananya Ingale
- EmpID: EMP123
- Basic Monthly Salary: 50000
- Special Allowances: 10000
- Bonus Percentage: 10

**Expected Output:**
- All inputs are valid ✔
- Gross Monthly Salary: ₹60000.00
- Annual Gross Salary: ₹792000.00

---

## Test Case 2: Valid inputs with zero special allowances
**Input:**
- Name: Rahul Sharma
- EmpID: RS789
- Basic Monthly Salary: 40000
- Special Allowances: 0
- Bonus Percentage: 5

**Expected Output:**
- All inputs are valid ✔
- Gross Monthly Salary: ₹40000.00
- Annual Gross Salary: ₹504000.00

---

## Test Case 3: Valid inputs with zero bonus
**Input:**
- Name: Sneha Patil
- EmpID: SP456
- Basic Monthly Salary: 35000
- Special Allowances: 5000
- Bonus Percentage: 0

**Expected Output:**
- All inputs are valid ✔
- Gross Monthly Salary: ₹40000.00
- Annual Gross Salary: ₹480000.00

---

## Test Case 4: Name is empty
**Input:**
- Name: (empty)

**Expected Output:**
- Error: Name cannot be empty.
- Prompt repeats for Name

---

## Test Case 5: Name contains numbers
**Input:**
- Name: Ananya123

**Expected Output:**
- Error: Name must contain alphabets only.
- Prompt repeats for Name

---

## Test Case 6: Name contains special characters
**Input:**
- Name: Rahul@#

**Expected Output:**
- Error: Name must contain alphabets only.
- Prompt repeats for Name

---

## Test Case 7: Name exceeds 50 characters
**Input:**
- Name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

**Expected Output:**
- Error: Name must not exceed 50 characters.
- Prompt repeats for Name

---

## Test Case 8: Valid name at 50-character boundary
**Input:**
- Name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

**Expected Output:**
- Accepted as valid name

---

## Test Case 9: EmpID contains special characters
**Input:**
- EmpID: EMP@12

**Expected Output:**
- Error: EmpID must be alphanumeric.
- Prompt repeats for EmpID

---

## Test Case 10: EmpID too short
**Input:**
- EmpID: E12

**Expected Output:**
- Error: EmpID length must be between 5 and 10 characters.
- Prompt repeats for EmpID

---

## Test Case 11: EmpID too long
**Input:**
- EmpID: EMPLOYEE12345

**Expected Output:**
- Error: EmpID length must be between 5 and 10 characters.
- Prompt repeats for EmpID

---

## Test Case 12: Valid EmpID at boundary length (5 chars)
**Input:**
- EmpID: EMP12

**Expected Output:**
- Accepted as valid EmpID

---

## Test Case 13: Basic salary is zero (not allowed)
**Input:**
- Basic Monthly Salary: 0

**Expected Output:**
- Error: Value must be positive.
- Prompt repeats for Basic Monthly Salary

---

## Test Case 14: Basic salary is negative
**Input:**
- Basic Monthly Salary: -40000

**Expected Output:**
- Error: Value must be positive.
- Prompt repeats for Basic Monthly Salary

---

## Test Case 15: Basic salary exceeds maximum limit
**Input:**
- Basic Monthly Salary: 20000000

**Expected Output:**
- Error: Value must not exceed ₹1,00,00,000.
- Prompt repeats for Basic Monthly Salary

---

## Test Case 16: Special allowances negative
**Input:**
- Special Allowances: -5000

**Expected Output:**
- Error: Value must be positive.
- Prompt repeats for Special Allowances

---

## Test Case 17: Special allowances exceed maximum limit
**Input:**
- Special Allowances: 15000000

**Expected Output:**
- Error: Value must not exceed ₹1,00,00,000.
- Prompt repeats for Special Allowances

---

## Test Case 18: Non-numeric salary input
**Input:**
- Basic Monthly Salary: abc

**Expected Output:**
- Error: Please enter numeric values only.
- Prompt repeats for salary

---

## Test Case 19: Bonus percentage negative
**Input:**
- Bonus Percentage: -5

**Expected Output:**
- Error: Bonus percentage must be between 0 and 100.
- Prompt repeats for Bonus Percentage

---

## Test Case 20: Bonus percentage greater than 100
**Input:**
- Bonus Percentage: 120

**Expected Output:**
- Error: Bonus percentage must be between 0 and 100.
- Prompt repeats for Bonus Percentage

---

## Test Case 21: Bonus percentage at upper boundary
**Input:**
- Bonus Percentage: 100

**Expected Output:**
- Accepted as valid bonus percentage

---

## Test Case 22: Gross monthly salary equals zero
**Input:**
- Basic Monthly Salary: 0
- Special Allowances: 0

**Expected Output:**
- Error: Gross Monthly Salary must be greater than zero.
- Program terminates

---

## Test Case 23: Annual gross salary exceeds realistic limit
**Input:**
- Basic Monthly Salary: 3000000
- Special Allowances: 2000000
- Bonus Percentage: 100

**Expected Output:**
- Error: Annual Gross Salary exceeds realistic limits.
- Program terminates

---

## Test Case 24: Decimal salary values
**Input:**
- Name: Pooja Kulkarni
- EmpID: PK789
- Basic Monthly Salary: 45500.75
- Special Allowances: 3499.25
- Bonus Percentage: 7.5

**Expected Output:**
- All inputs are valid ✔
- Gross Monthly Salary: ₹49000.00
- Annual Gross Salary: ₹632100.00
