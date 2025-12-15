# Test Cases for Income Tax Calculation Program (New Regime with 87A Rebate)

## Test Case 1: Taxable income = 0
**Input:**
- Taxable Income: 0

**Expected Output:**
- Section 87A Rebate Applied: 100%
- Tax before Cess: ₹0.00
- Total Tax Payable: ₹0.00

---

## Test Case 2: Taxable income below rebate limit
**Input:**
- Taxable Income: 500000

**Expected Output:**
- Section 87A Rebate Applied: 100%
- Tax before Cess: ₹0.00
- Total Tax Payable: ₹0.00

---

## Test Case 3: Taxable income exactly at rebate limit
**Input:**
- Taxable Income: 700000

**Expected Output:**
- Section 87A Rebate Applied: 100%
- Tax before Cess: ₹0.00
- Total Tax Payable: ₹0.00

---

## Test Case 4: Taxable income just above rebate limit
**Input:**
- Taxable Income: 700001

**Expected Output:**
- Tax before Cess: ₹20000.05
- Health & Education Cess (4%): ₹800.00
- Total Tax Payable: ₹20800.05

---

## Test Case 5: Taxable income at first slab limit
**Input:**
- Taxable Income: 300000

**Expected Output:**
- Section 87A Rebate Applied: 100%
- Tax before Cess: ₹0.00
- Total Tax Payable: ₹0.00

---

## Test Case 6: Taxable income at second slab limit
**Input:**
- Taxable Income: 600000

**Expected Output:**
- Section 87A Rebate Applied: 100%
- Tax before Cess: ₹0.00
- Total Tax Payable: ₹0.00

---

## Test Case 7: Taxable income at third slab limit
**Input:**
- Taxable Income: 900000

**Expected Output:**
- Tax before Cess: ₹30000.00
- Health & Education Cess (4%): ₹1200.00
- Total Tax Payable: ₹31200.00

---

## Test Case 8: Taxable income at fourth slab limit
**Input:**
- Taxable Income: 1200000

**Expected Output:**
- Tax before Cess: ₹60000.00
- Health & Education Cess (4%): ₹2400.00
- Total Tax Payable: ₹62400.00

---

## Test Case 9: Taxable income at fifth slab limit
**Input:**
- Taxable Income: 1500000

**Expected Output:**
- Tax before Cess: ₹105000.00
- Health & Education Cess (4%): ₹4200.00
- Total Tax Payable: ₹109200.00

---

## Test Case 10: Taxable income above highest slab
**Input:**
- Taxable Income: 2000000

**Expected Output:**
- Tax before Cess: ₹255000.00
- Health & Education Cess (4%): ₹10200.00
- Total Tax Payable: ₹265200.00

---

## Test Case 11: Taxable income with decimal value
**Input:**
- Taxable Income: 845000.50

**Expected Output:**
- Tax before Cess: ₹24500.05
- Health & Education Cess (4%): ₹980.00
- Total Tax Payable: ₹25480.05

---

## Test Case 12: Very large taxable income
**Input:**
- Taxable Income: 10000000

**Expected Output:**
- Tax before Cess: ₹2175000.00
- Health & Education Cess (4%): ₹87000.00
- Total Tax Payable: ₹2262000.00

---

## Test Case 13: Negative taxable income
**Input:**
- Taxable Income: -500000

**Expected Output:**
- Please enter a positive number.
- Prompt repeats for Taxable Income

---

## Test Case 14: Non-numeric taxable income (alphabetic)
**Input:**
- Taxable Income: abc

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Taxable Income

---

## Test Case 15: Non-numeric taxable income (special characters)
**Input:**
- Taxable Income: @@@

**Expected Output:**
- Invalid input! Please enter a numeric value.
- Prompt repeats for Taxable Income

---

## Test Case 16: Input with leading and trailing spaces
**Input:**
- Taxable Income:   800000  

**Expected Output:**
- Tax before Cess: ₹25000.00
- Health & Education Cess (4%): ₹1000.00
- Total Tax Payable: ₹26000.00
