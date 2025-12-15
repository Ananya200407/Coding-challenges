# Test Cases for Printing Odd Number Series up to N

---

## Test Case 1: Valid small positive integer
**Input:**
- N: 10

**Expected Output:**
- Odd number series up to 10 is:
- 1, 3, 5, 7, 9

---

## Test Case 2: Valid odd number
**Input:**
- N: 9

**Expected Output:**
- Odd number series up to 9 is:
- 1, 3, 5, 7, 9

---

## Test Case 3: Boundary case (minimum valid input)
**Input:**
- N: 1

**Expected Output:**
- Odd number series up to 1 is:
- 1

---

## Test Case 4: Small even number
**Input:**
- N: 2

**Expected Output:**
- Odd number series up to 2 is:
- 1

---

## Test Case 5: N equals zero
**Input:**
- N: 0

**Expected Output:**
- Please enter a positive integer greater than 0.

---

## Test Case 6: Negative integer
**Input:**
- N: -5

**Expected Output:**
- Please enter a positive integer greater than 0.

---

## Test Case 7: Non-numeric input (alphabetic)
**Input:**
- N: abc

**Expected Output:**
- Invalid input! Please enter an integer value.

---

## Test Case 8: Non-numeric input (special characters)
**Input:**
- N: #$%

**Expected Output:**
- Invalid input! Please enter an integer value.

---

## Test Case 9: Decimal input
**Input:**
- N: 7.5

**Expected Output:**
- Invalid input! Please enter an integer value.

---

## Test Case 10: Large valid input
**Input:**
- N: 50

**Expected Output:**
- Odd number series up to 50 is:
- 1, 3, 5, ..., 49
