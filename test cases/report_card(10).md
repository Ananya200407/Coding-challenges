# Test Cases for Student Report Card Program

## Test Case 1: Valid name, average >= 60 (1st Class)
**Input:**
- Name: Ananya
- Subject 1 Marks: 75
- Subject 2 Marks: 68
- Subject 3 Marks: 70

**Expected Output:**
- Class Secured: 1st Class

---

## Test Case 2: Valid name, average between 50 and 59.99 (2nd Class)
**Input:**
- Name: Rahul
- Subject 1 Marks: 55
- Subject 2 Marks: 52
- Subject 3 Marks: 50

**Expected Output:**
- Class Secured: 2nd Class

---

## Test Case 3: Valid name, average between 35 and 49.99 (Pass Class)
**Input:**
- Name: Sneha
- Subject 1 Marks: 40
- Subject 2 Marks: 38
- Subject 3 Marks: 45

**Expected Output:**
- Class Secured: Pass Class

---

## Test Case 4: Valid name, average below 35 (Fail)
**Input:**
- Name: Ramesh
- Subject 1 Marks: 30
- Subject 2 Marks: 25
- Subject 3 Marks: 20

**Expected Output:**
- Class Secured: Fail

---

## Test Case 5: Boundary case – average exactly 60
**Input:**
- Name: Pooja
- Subject 1 Marks: 60
- Subject 2 Marks: 60
- Subject 3 Marks: 60

**Expected Output:**
- Class Secured: 1st Class

---

## Test Case 6: Boundary case – average exactly 50
**Input:**
- Name: Kiran
- Subject 1 Marks: 50
- Subject 2 Marks: 50
- Subject 3 Marks: 50

**Expected Output:**
- Class Secured: 2nd Class

---

## Test Case 7: Boundary case – average exactly 35
**Input:**
- Name: Meena
- Subject 1 Marks: 35
- Subject 2 Marks: 35
- Subject 3 Marks: 35

**Expected Output:**
- Class Secured: Pass Class

---

## Test Case 8: Maximum marks
**Input:**
- Name: Arjun
- Subject 1 Marks: 100
- Subject 2 Marks: 100
- Subject 3 Marks: 100

**Expected Output:**
- Class Secured: 1st Class

---

## Test Case 9: Minimum valid marks
**Input:**
- Name: Nisha
- Subject 1 Marks: 0
- Subject 2 Marks: 0
- Subject 3 Marks: 0

**Expected Output:**
- Class Secured: Fail

---

## Test Case 10: Marks greater than 100
**Input:**
- Name: Aman
- Subject 1 Marks: 105
- Subject 2 Marks: 90
- Subject 3 Marks: 85

**Expected Output:**
- Invalid marks! Marks should be between 0 and 100.

---

## Test Case 11: Negative marks
**Input:**
- Name: Riya
- Subject 1 Marks: -10
- Subject 2 Marks: 50
- Subject 3 Marks: 60

**Expected Output:**
- Invalid marks! Marks should be between 0 and 100.

---

## Test Case 12: Decimal marks
**Input:**
- Name: Suresh
- Subject 1 Marks: 78.5
- Subject 2 Marks: 82.3
- Subject 3 Marks: 69.2

**Expected Output:**
- Class Secured: 1st Class

---

## Test Case 13: Empty name
**Input:**
- Name: (empty)
- Subject 1 Marks: 60
- Subject 2 Marks: 70
- Subject 3 Marks: 80

**Expected Output:**
- Invalid name! Name should contain alphabets only.

---

## Test Case 14: Name with numbers
**Input:**
- Name: Ananya123
- Subject 1 Marks: 60
- Subject 2 Marks: 70
- Subject 3 Marks: 80

**Expected Output:**
- Invalid name! Name should contain alphabets only.

---

## Test Case 15: Name with special characters
**Input:**
- Name: Rahul@#
- Subject 1 Marks: 65
- Subject 2 Marks: 75
- Subject 3 Marks: 85

**Expected Output:**
- Invalid name! Name should contain alphabets only.

---

## Test Case 16: Name with spaces (valid)
**Input:**
- Name: Ananya Ingale
- Subject 1 Marks: 70
- Subject 2 Marks: 72
- Subject 3 Marks: 74

**Expected Output:**
- Class Secured: 1st Class

---

## Test Case 17: Non-numeric marks input
**Input:**
- Name: Karthik
- Subject 1 Marks: abc
- Subject 2 Marks: 60
- Subject 3 Marks: 70

**Expected Output:**
- Invalid input! Please enter numeric values for marks.

---

## Test Case 18: Marks entered as special characters
**Input:**
- Name: Divya
- Subject 1 Marks: @@@
- Subject 2 Marks: 60
- Subject 3 Marks: 70

**Expected Output:**
- Invalid input! Please enter numeric values for marks.
