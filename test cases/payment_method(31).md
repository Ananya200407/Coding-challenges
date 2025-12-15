# Test Cases: Item Billing with PROMO10 and Payment Method Surcharge


## Test Case 1: Single item, no promo, cash payment
**Input:**
1
A101
Pen
5
100
cash


**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: A101
Description: Pen
Quantity: 5
Price per item: 100
Item Total: Rs. 500.0

Subtotal after discounts: Rs. 500.0
Select payment method (cash/card): cash
No surcharge applied for Cash payment.

------ PAYMENT SUMMARY ------
Payment Method: Cash
Surcharge: Rs. 0.0
Final Payable Amount: Rs. 500.0


## Test Case 2: Single item, PROMO10, card payment
**Input:**
1
PROMO10
Notebook
10
200
card

**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: PROMO10
Description: Notebook
Quantity: 10
Price per item: 200
Promotional Discount Applied (10%): -Rs. 200.0
Item Total: Rs. 1800.0

Subtotal after discounts: Rs. 1800.0
Select payment method (cash/card): card
2% Credit Card Surcharge Applied: +Rs. 36.0

------ PAYMENT SUMMARY ------
Payment Method: Credit Card
Surcharge: Rs. 36.0
Final Payable Amount: Rs. 1836.0


## Test Case 3: Multiple items, mixed promo, cash payment
**Input:**
3
PROMO10
Chair
2
1500
B202
Desk
1
3000
C303
Lamp
4
500
cash

**Output:**
Enter number of items: 3

Enter details for Item 1
Item code: PROMO10
Description: Chair
Quantity: 2
Price per item: 1500
Promotional Discount Applied (10%): -Rs. 300.0
Item Total: Rs. 2700.0

Enter details for Item 2
Item code: B202
Description: Desk
Quantity: 1
Price per item: 3000
Item Total: Rs. 3000.0

Enter details for Item 3
Item code: C303
Description: Lamp
Quantity: 4
Price per item: 500
Item Total: Rs. 2000.0

Subtotal after discounts: Rs. 7700.0
Select payment method (cash/card): cash
No surcharge applied for Cash payment.

------ PAYMENT SUMMARY ------
Payment Method: Cash
Surcharge: Rs. 0.0
Final Payable Amount: Rs. 7700.0


## Test Case 4: Negative quantity skipped
**Input:**
2
D404
Mouse
-3
500
E505
Keyboard
2
1000
card

**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: D404
Description: Mouse
Quantity: -3
Price per item: 500
Quantity and price must be non-negative. Item skipped.

Enter details for Item 2
Item code: E505
Description: Keyboard
Quantity: 2
Price per item: 1000
Item Total: Rs. 2000.0

Subtotal after discounts: Rs. 2000.0
Select payment method (cash/card): card
2% Credit Card Surcharge Applied: +Rs. 40.0

------ PAYMENT SUMMARY ------
Payment Method: Credit Card
Surcharge: Rs. 40.0
Final Payable Amount: Rs. 2040.0

## Test Case 5: All items PROMO10, card payment
**Input:**
2
PROMO10
Table
3
2000
PROMO10
Lamp
5
500
card

**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: PROMO10
Description: Table
Quantity: 3
Price per item: 2000
Promotional Discount Applied (10%): -Rs. 600.0
Item Total: Rs. 5400.0

Enter details for Item 2
Item code: PROMO10
Description: Lamp
Quantity: 5
Price per item: 500
Promotional Discount Applied (10%): -Rs. 250.0
Item Total: Rs. 2250.0

Subtotal after discounts: Rs. 7650.0
Select payment method (cash/card): card
2% Credit Card Surcharge Applied: +Rs. 153.0

------ PAYMENT SUMMARY ------
Payment Method: Credit Card
Surcharge: Rs. 153.0
Final Payable Amount: Rs. 7803.0


## Test Case 6: Invalid payment method
**Input:**
1
F606
Mouse
2
200
cheque

**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: F606
Description: Mouse
Quantity: 2
Price per item: 200
Item Total: Rs. 400.0

Subtotal after discounts: Rs. 400.0
Select payment method (cash/card): cheque
Invalid payment method selected. No surcharge applied.

------ PAYMENT SUMMARY ------
Payment Method: Unknown
Surcharge: Rs. 0.0
Final Payable Amount: Rs. 400.0

## Test Case 7: Invalid numeric input
**Input:**
abc

**Output:**
Invalid input! Please enter numeric values correctly.

