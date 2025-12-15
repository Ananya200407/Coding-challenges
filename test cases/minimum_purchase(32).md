# Test Cases: Item Billing with PROMO10, Tax, Surcharge, Minimum Purchase

---

## Test Case 1: Single item, no promo, cash payment, total > 500
**Input:**
1
A101
5
200
cash


**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: A101
Quantity: 5
Price per item: 200

Select payment method (cash/card): cash

========== INVOICE ==========
Subtotal: Rs. 1000.0
Tax (10%): Rs. 100.0
Surcharge: Rs. 0.0
Final Payable Amount: Rs. 1100.0


## Test Case 2: Single item, PROMO10, card payment
**Input:**
1
PROMO10
10
200
card


**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: PROMO10
Quantity: 10
Price per item: 200

Select payment method (cash/card): card

========== INVOICE ==========
Subtotal: Rs. 1800.0
Tax (10%): Rs. 180.0
Surcharge: Rs. 39.6
Final Payable Amount: Rs. 2019.6


---

## Test Case 3: Multiple items, mixed promo, cash
**Input:**
3
PROMO10
2
1500
B202
1
3000
C303
4
500
cash


**Output:**
Enter number of items: 3

Enter details for Item 1
Item code: PROMO10
Quantity: 2
Price per item: 1500

Enter details for Item 2
Item code: B202
Quantity: 1
Price per item: 3000

Enter details for Item 3
Item code: C303
Quantity: 4
Price per item: 500

Select payment method (cash/card): cash

========== INVOICE ==========
Subtotal: Rs. 7700.0
Tax (10%): Rs. 770.0
Surcharge: Rs. 0.0
Final Payable Amount: Rs. 8470.0


## Test Case 4: Negative quantity skipped
**Input:**
2
D404
-3
500
E505
2
1000
cash

**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: D404
Quantity: -3
Price per item: 500
Invalid quantity or price. Item skipped.

Enter details for Item 2
Item code: E505
Quantity: 2
Price per item: 1000

Select payment method (cash/card): cash

========== INVOICE ==========
Subtotal: Rs. 2000.0
Tax (10%): Rs. 200.0
Surcharge: Rs. 0.0
Final Payable Amount: Rs. 2200.0


## Test Case 5: Total below minimum ₹500
**Input:**
1
F606
1
400
cash

**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: F606
Quantity: 1
Price per item: 400

Select payment method (cash/card): cash

Minimum purchase amount of ₹500 not met.
Invoice cannot be generated.


## Test Case 6: All items PROMO10, card payment
**Input:**
2
PROMO10
3
2000
PROMO10
5
500
card

makefile
Copy code

**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: PROMO10
Quantity: 3
Price per item: 2000

Enter details for Item 2
Item code: PROMO10
Quantity: 5
Price per item: 500

Select payment method (cash/card): card

========== INVOICE ==========
Subtotal: Rs. 7650.0
Tax (10%): Rs. 765.0
Surcharge: Rs. 168.3
Final Payable Amount: Rs. 8583.3


## Test Case 7: Invalid numeric input
**Input:**
abc

**Output:**
Invalid input! Please enter numeric values correctly.

