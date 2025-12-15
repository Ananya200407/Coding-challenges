# Test Cases for Multiple Item Billing with Discounts & Tax


## Test Case 1: No discounts, tax 5%
**Input:**
1
A101
Pen
2
100
n



**Output:**
Enter number of items: 1

Enter details for Item 1
Item code: A101
Description: Pen
Quantity: 2
Price per item: 100
Item Total: Rs. 200.0

------ BILL SUMMARY ------
Total Quantity: 2
Subtotal: Rs. 200.0
Amount After Discounts: Rs. 200.0
Tax Applied (5%): Rs. 10.0
Final Payable Amount: Rs. 210.0


## Test Case 2: 10% discount only, tax 10%
**Input:**
2
B202
Chair
10
800
C303
Table
5
1200
n


**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: B202
Description: Chair
Quantity: 10
Price per item: 800
Item Total: Rs. 8000.0

Enter details for Item 2
Item code: C303
Description: Table
Quantity: 5
Price per item: 1200
Item Total: Rs. 6000.0

------ BILL SUMMARY ------
Total Quantity: 15
Subtotal: Rs. 14000.0
10% Discount Applied: -Rs. 1400.0
Amount After Discounts: Rs. 12600.0
Tax Applied (10%): Rs. 1260.0
Final Payable Amount: Rs. 13860.0


## Test Case 3: 5% quantity discount only, tax 5%
**Input:**
2
D404
Pen
15
100
E505
Notebook
10
50
n


**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: D404
Description: Pen
Quantity: 15
Price per item: 100
Item Total: Rs. 1500.0

Enter details for Item 2
Item code: E505
Description: Notebook
Quantity: 10
Price per item: 50
Item Total: Rs. 500.0

------ BILL SUMMARY ------
Total Quantity: 25
Subtotal: Rs. 2000.0
5% Quantity Discount Applied: -Rs. 100.0
Amount After Discounts: Rs. 1900.0
Tax Applied (5%): Rs. 95.0
Final Payable Amount: Rs. 1995.0

## Test Case 4: 2% membership discount only, tax 5%
**Input:**
2
F606
Mouse
2
2000
G707
Keyboard
1
3000


**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: F606
Description: Mouse
Quantity: 2
Price per item: 2000
Item Total: Rs. 4000.0

Enter details for Item 2
Item code: G707
Description: Keyboard
Quantity: 1
Price per item: 3000
Item Total: Rs. 3000.0

------ BILL SUMMARY ------
Total Quantity: 3
Subtotal: Rs. 7000.0
2% Membership Discount Applied: -Rs. 140.0
Amount After Discounts: Rs. 6860.0
Tax Applied (10%): Rs. 686.0
Final Payable Amount: Rs. 7546.0


## Test Case 5: Both 10% and 5% discounts, no membership, tax 10%
**Input:**
3
H808
Laptop
10
800
I909
Mousepad
15
200
J010
Monitor
5
1000
n

**Output:**
Enter number of items: 3

Enter details for Item 1
Item code: H808
Description: Laptop
Quantity: 10
Price per item: 800
Item Total: Rs. 8000.0

Enter details for Item 2
Item code: I909
Description: Mousepad
Quantity: 15
Price per item: 200
Item Total: Rs. 3000.0

Enter details for Item 3
Item code: J010
Description: Monitor
Quantity: 5
Price per item: 1000
Item Total: Rs. 5000.0

------ BILL SUMMARY ------
Total Quantity: 30
Subtotal: Rs. 16000.0
10% Discount Applied: -Rs. 1600.0
5% Quantity Discount Applied: -Rs. 720.0
Amount After Discounts: Rs. 13680.0
Tax Applied (10%): Rs. 1368.0
Final Payable Amount: Rs. 15048.0


## Test Case 6: All discounts applied, tax 15%
**Input:**
3
K111
Chair
10
800
L212
Desk
15
1200
M313
Lamp
5
1000

**Output:**
Enter number of items: 3

Enter details for Item 1
Item code: K111
Description: Chair
Quantity: 10
Price per item: 800
Item Total: Rs. 8000.0

Enter details for Item 2
Item code: L212
Description: Desk
Quantity: 15
Price per item: 1200
Item Total: Rs. 18000.0

Enter details for Item 3
Item code: M313
Description: Lamp
Quantity: 5
Price per item: 1000
Item Total: Rs. 5000.0

------ BILL SUMMARY ------
Total Quantity: 30
Subtotal: Rs. 31000.0
10% Discount Applied: -Rs. 3100.0
5% Quantity Discount Applied: -Rs. 1395.0
2% Membership Discount Applied: -Rs. 574.1
Amount After Discounts: Rs. 26030.9
Tax Applied (15%): Rs. 3904.64
Final Payable Amount: Rs. 29935.54


## Test Case 7: Invalid input
**Input:**
abc

**Output:**
Invalid input! Please enter numeric values correctly.


