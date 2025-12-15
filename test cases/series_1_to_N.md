# Test Cases for Printing Series up to N

---

## Test Case 1: Valid small positive integer
**Input:**
- N: 5

**Expected Output:**
- Series up to 5 is:
- 1, 2, 3, 4, 5

---

## Test Case 2: Valid single value (boundary case)
**Input:**
- N: 1

**Expected Output:**
- Series up to 1 is:
- 1

---

## Test Case 3: Valid medium positive integer
**Input:**
- N: 10

**Expected Output:**
- Series up to 10 is:
- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

---

## Test Case 4: N equals zero
**Input:**
- N: 0

**Expected Output:**
- Please enter a positive integer greater than 0.

---

## Test Case 5: Negative integer
**Input:**
- N: -7

**Expected Output:**
- Please enter a positive integer greater than 0.

---

## Test Case 6: Non-numeric input (alphabetic)
**Input:**
- N: abc

**Expected Output:**
- Invalid input! Please enter an integer value.

---

## Test Case 7: Non-numeric input (special characters)
**Input:**
- N: @@@

**Expected Output:**
- Invalid input! Please enter an integer value.

---

## Test Case 8: Decimal number input
**Input:**
- N: 5.5

**Expected Output:**
- Invalid input! Please enter an integer value.

---

## Test Case 9: Very large positive integer
**Input:**
- N: 100

**Expected Output:**
- Series up to 100 is:
- 1, 2, 3, ..., 100

---

## Test Case 10: Input with leading and trailing spaces
**Input:**
- N:   7  

**Expected Output:**
- Series up to 7 is:
- 1, 2, 3, 4, 5, 6, 7
