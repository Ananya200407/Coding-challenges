# Test Cases for Complex Series up to N

---

## Test Case 1: N = 50
**Input:**
- Maximum value N: 50

**Expected Output:**
- Series up to 50 is:
- 1, 4, 7, 12, 23, 45

**Explanation:**  
- Start = 1  
- 2nd term: 1 + 3 → 4  
- 3rd term: 4 + 3 → 7  
- 4th term: 7 + 5 → 12  
- 5th term: 12 + 11 → 23  
- 6th term: 23 + (23-12)*2 = 45  
- Next term 45 + (45-23)*2 = 89 > 50 → stop

---

## Test Case 2: N = 12
**Input:**
- Maximum value N: 12

**Expected Output:**
- Series up to 12 is:
- 1, 4, 7, 12

---

## Test Case 3: N = 7
**Input:**
- Maximum value N: 7

**Expected Output:**
- Series up to 7 is:
- 1, 4, 7

---

## Test Case 4: N = 1 (minimum value)
**Input:**
- Maximum value N: 1

**Expected Output:**
- Series up to 1 is:
- 1

---

## Test Case 5: N < 1
**Input:**
- Maximum value N: 0

**Expected Output:**
- No terms in the series for N < 0

---

## Test Case 6: Negative input
**Input:**
- Maximum value N: -10

**Expected Output:**
- No terms in the series for N < -10

---

## Test Case 7: Non-numeric input
**Input:**
- Maximum value N: abc

**Expected Output:**
- Invalid input! Please enter a positive integer.

---

## Test Case 8: N = 45
**Input:**
- Maximum value N: 45

**Expected Output:**
- Series up to 45 is:
- 1, 4, 7, 12, 23, 45

---

## Test Case 9: Leading/trailing spaces in input
**Input:**
- Maximum value N: "   20  "

**Expected Output:**
- Series up to 20 is:
- 1, 4, 7, 12

---

## Test Case 10: Large N = 100
**Input:**
- Maximum value N: 100

**Expected Output:**
- Series up to 100 is:
- 1, 4, 7, 12, 23, 45, 89
