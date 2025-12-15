# Test Cases for Series of Squares of Even Numbers up to N

---

## Test Case 1: N = 16 (perfect square included)
**Input:**
- N: 16

**Expected Output:**
- Series up to 16 is:
- 4, 16

---

## Test Case 2: N = 20 (non-perfect square)
**Input:**
- N: 20

**Expected Output:**
- Series up to 20 is:
- 4, 16

---

## Test Case 3: N = 4 (minimum valid series)
**Input:**
- N: 4

**Expected Output:**
- Series up to 4 is:
- 4

---

## Test Case 4: N < 4 (no numbers in series)
**Input:**
- N: 3

**Expected Output:**
- There are no numbers in the series up to 3

---

## Test Case 5: N = 10
**Input:**
- N: 10

**Expected Output:**
- Series up to 10 is:
- 4

---

## Test Case 6: N = 0
**Input:**
- N: 0

**Expected Output:**
- There are no numbers in the series up to 0

---

## Test Case 7: Negative input
**Input:**
- N: -5

**Expected Output:**
- There are no numbers in the series up to -5

---

## Test Case 8: Non-numeric input (alphabetic)
**Input:**
- N: abc

**Expected Output:**
- Invalid input! Please enter a positive integer.

---

## Test Case 9: Non-numeric input (special characters)
**Input:**
- N: @#

**Expected Output:**
- Invalid input! Please enter a positive integer.

---

## Test Case 10: Large N
**Input:**
- N: 100

**Expected Output:**
- Series up to 100 is:
- 4, 16, 36, 64, 100
