## Test Case 1: Valid name, salary greater than 300000
**Input:**
- Name: Ananya
- Salary: 500000

**Expected Output:**
- Ananya must pay tax.

---

## Test Case 2: Valid name, salary exactly 300000
**Input:**
- Name: Rahul
- Salary: 300000

**Expected Output:**
- Rahul does not need to pay tax.

---

## Test Case 3: Valid name, salary less than 300000
**Input:**
- Name: Sneha
- Salary: 250000

**Expected Output:**
- Sneha does not need to pay tax.

---

## Test Case 4: Valid name with spaces, salary greater than 300000
**Input:**
- Name: Ananya Ingale
- Salary: 450000

**Expected Output:**
- Ananya Ingale must pay tax.

---

## Test Case 5: Valid name with leading and trailing spaces
**Input:**
- Name:   Rohit Sharma  
- Salary: 350000

**Expected Output:**
- Rohit Sharma must pay tax.

---

## Test Case 6: Empty name
**Input:**
- Name: (empty)
- Salary: 200000

**Expected Output:**
- Invalid name! Name should contain alphabets only.

---

## Test Case 7: Name with numbers
**Input:**
- Name: Ananya123
- Salary: 400000

**Expected Output:**
- Invalid name! Name should contain alphabets only.

---

## Test Case 8: Name with special characters
**Input:**
- Name: Ananya@#
- Salary: 400000

**Expected Output:**
- Invalid name! Name should contain alphabets only.

---

## Test Case 9: Name with only spaces
**Input:**
- Name: "   "
- Salary: 200000

**Expected Output:**
- Invalid name! Name should contain alphabets only.

---

## Test Case 10: Negative salary
**Input:**
- Name: Meena
- Salary: -50000

**Expected Output:**
- Salary cannot be negative.

---

## Test Case 11: Salary as non-numeric value
**Input:**
- Name: Kiran
- Salary: abc

**Expected Output:**
- Invalid input! Please enter numeric value for salary.

---

## Test Case 12: Salary as special characters
**Input:**
- Name: Suresh
- Salary: @@@

**Expected Output:**
- Invalid input! Please enter numeric value for salary.

---

## Test Case 13: Salary as decimal value
**Input:**
- Name: Pooja
- Salary: 350000.75

**Expected Output:**
- Pooja must pay tax.

---

## Test Case 14: Salary equals zero
**Input:**
- Name: Ramesh
- Salary: 0

**Expected Output:**
- Ramesh does not need to pay tax.

---

## Test Case 15: Single character name
**Input:**
- Name: A
- Salary: 400000

**Expected Output:**
- A must pay tax.
