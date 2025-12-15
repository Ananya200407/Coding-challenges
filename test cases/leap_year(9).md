# Test Cases for Leap Year Program

## Test Case 1: Typical leap year divisible by 4
**Input:**
- Year: 2024

**Expected Output:**
- 2024 is a Leap Year.

---

## Test Case 2: Common year not divisible by 4
**Input:**
- Year: 2023

**Expected Output:**
- 2023 is not a Leap Year.

---

## Test Case 3: Century year not divisible by 400
**Input:**
- Year: 1900

**Expected Output:**
- 1900 is not a Leap Year.

---

## Test Case 4: Century year divisible by 400
**Input:**
- Year: 2000

**Expected Output:**
- 2000 is a Leap Year.

---

## Test Case 5: Year divisible by 100 but not by 400
**Input:**
- Year: 2100

**Expected Output:**
- 2100 is not a Leap Year.

---

## Test Case 6: Year divisible by 4 but not by 100
**Input:**
- Year: 2016

**Expected Output:**
- 2016 is a Leap Year.

---

## Test Case 7: Smallest valid positive year
**Input:**
- Year: 1

**Expected Output:**
- 1 is not a Leap Year.

---

## Test Case 8: Year zero
**Input:**
- Year: 0

**Expected Output:**
- Invalid year! Please enter a positive integer.

---

## Test Case 9: Negative year
**Input:**
- Year: -2024

**Expected Output:**
- Invalid year! Please enter a positive integer.

---

## Test Case 10: Large leap year
**Input:**
- Year: 2400

**Expected Output:**
- 2400 is a Leap Year.

---

## Test Case 11: Large non-leap year
**Input:**
- Year: 2500

**Expected Output:**
- 2500 is not a Leap Year.

---

## Test Case 12: Non-numeric input (alphabetic)
**Input:**
- Year: abc

**Expected Output:**
- Invalid input! Please enter a valid integer for the year.

---

## Test Case 13: Non-numeric input (special characters)
**Input:**
- Year: @@@

**Expected Output:**
- Invalid input! Please enter a valid integer for the year.

---

## Test Case 14: Decimal input
**Input:**
- Year: 2024.5

**Expected Output:**
- Invalid input! Please enter a valid integer for the year.

---

## Test Case 15: Leading and trailing spaces
**Input:**
- Year:   2020  

**Expected Output:**
- 2020 is a Leap Year.
