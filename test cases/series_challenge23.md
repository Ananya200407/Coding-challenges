# Test Cases for Alternating Increment Series up to N

---

## Test Case 1: N = 20
**Input:**
- Maximum value N: 20

**Expected Output:**
- Series up to 20 is:
- 1, 5, 9, 13, 21

**Explanation:**
- Start = 1  
- +4 → 5, +4 → 9, +4 → 13, +8 → 21 (4th term increment = 8)  

---

## Test Case 2: N = 10
**Input:**
- Maximum value N: 10

**Expected Output:**
- Series up to 10 is:
- 1, 5, 9

---

## Test Case 3: N = 1 (minimum value)
**Input:**
- Maximum value N: 1

**Expected Output:**
- Series up to 1 is:
- 1

---

## Test Case 4: N = 0
**Input:**
- Maximum value N: 0

**Expected Output:**
- No terms in the series for N < 0

---

## Test Case 5: Negative input
**Input:**
- Maximum value N: -5

**Expected Output:**
- No terms in the series for N < -5

---

## Test Case 6: Non-numeric input
**Input:**
- Maximum value N: abc

**Expected Output:**
- Invalid input! Please enter a positive integer.

---

## Test Case 7: Series with multiple 4th term increments
**Input:**
- Maximum value N: 50

**Expected Output:**
- Series up to 50 is:
- 1, 5, 9, 13, 21, 25, 29, 33, 41, 45, 49

**Explanation:**  
- Increments: +4 normally, +8 on every 4th term (1-based index)

---

## Test Case 8: N smaller than first increment
**Input:**
- Maximum value N: 3

**Expected Output:**
- Series up to 3 is:
- 1

---

## Test Case 9: Leading/trailing spaces in input
**Input:**
- Maximum value N: "   12  "

**Expected Output:**
- Series up to 12 is:
- 1, 5, 9

---

## Test Case 10: Large N
**Input:**
- Maximum value N: 100

**Expected Output:**
- Series up to 100 is:
- 1, 5, 9, 13, 21, 25, 29, 33, 41, 45, 49, 53, 61, 65, 69, 73, 81, 85, 89, 97
