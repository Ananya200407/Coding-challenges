# Test Cases for Item Billing with Promotional Discount


## Test Case 1: Single item, no promo
**Input:**
1
A101
Pen
5
100


**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: A101
Description: Pen
Quantity: 5
Price per item: 100
No Promotional Discount Applied
Final Item Total: Rs. 500.0

========================
Grand Total: Rs. 500.0


## Test Case 2: Single item, with PROMO10
**Input:**
1
PROMO10
Notebook
10
200


**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: PROMO10
Description: Notebook
Quantity: 10
Price per item: 200
Promotional Discount Applied (10%): -Rs. 200.0
Final Item Total: Rs. 1800.0

========================
Grand Total: Rs. 1800.0


## Test Case 3: Multiple items, mixed promo
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


**Output:**
Enter number of items: 3

Enter details for Item 1
Item code: PROMO10
Description: Chair
Quantity: 2
Price per item: 1500
Promotional Discount Applied (10%): -Rs. 300.0
Final Item Total: Rs. 2700.0

Enter details for Item 2
Item code: B202
Description: Desk
Quantity: 1
Price per item: 3000
No Promotional Discount Applied
Final Item Total: Rs. 3000.0

Enter details for Item 3
Item code: C303
Description: Lamp
Quantity: 4
Price per item: 500
No Promotional Discount Applied
Final Item Total: Rs. 2000.0

========================
Grand Total: Rs. 7700.0


## Test Case 4: Negative quantity (skipped)
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
No Promotional Discount Applied
Final Item Total: Rs. 2000.0

========================
Grand Total: Rs. 2000.0


## Test Case 5: Negative price (skipped)
**Input:**
1
PROMO10
Chair
2
-1500

**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: PROMO10
Description: Chair
Quantity: 2
Price per item: -1500
Quantity and price must be non-negative. Item skipped.

========================
Grand Total: Rs. 0.0

## Test Case 6: All items with PROMO10
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

**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: PROMO10
Description: Table
Quantity: 3
Price per item: 2000
Promotional Discount Applied (10%): -Rs. 600.0
Final Item Total: Rs. 5400.0

Enter details for Item 2
Item code: PROMO10
Description: Lamp
Quantity: 5
Price per item: 500
Promotional Discount Applied (10%): -Rs. 250.0
Final Item Total: Rs. 2250.0

========================
Grand Total: Rs. 7650.0


## Test Case 7: Invalid input (non-numeric)
**Input:**
abc


**Output:**
Invalid input! Please enter numeric values correctly.


