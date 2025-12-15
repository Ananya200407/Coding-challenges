# Test Cases for Multiple Item Billing with All Discounts


## Test Case 1: No discounts applied
**Input:**
2
A101
Pen
5
100
B202
Notebook
10
200
n


**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: A101
Description: Pen
Quantity: 5
Price per item: 100
Item Total: Rs. 500.0

Enter details for Item 2
Item code: B202
Description: Notebook
Quantity: 10
Price per item: 200
Item Total: Rs. 2000.0

------ BILL SUMMARY ------
Total Quantity: 15
Initial Grand Total: Rs. 2500.0
No 10% Discount Applied
No Quantity Discount Applied
No Membership Discount Applied
Final Payable Amount: Rs. 2500.0


## Test Case 2: Only 10% discount applied
**Input:**
2
C303
Chair
10
800
D404
Table
5
1200
n



**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: C303
Description: Chair
Quantity: 10
Price per item: 800
Item Total: Rs. 8000.0

Enter details for Item 2
Item code: D404
Description: Table
Quantity: 5
Price per item: 1200
Item Total: Rs. 6000.0

------ BILL SUMMARY ------
Total Quantity: 15
Initial Grand Total: Rs. 14000.0
10% Discount Applied: -Rs. 1400.0
No Quantity Discount Applied
No Membership Discount Applied
Final Payable Amount: Rs. 12600.0


## Test Case 3: Only 5% quantity discount applied
**Input:**
2
E505
Pen
15
100
F606
Notebook
10
50
n



**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: E505
Description: Pen
Quantity: 15
Price per item: 100
Item Total: Rs. 1500.0

Enter details for Item 2
Item code: F606
Description: Notebook
Quantity: 10
Price per item: 50
Item Total: Rs. 500.0

------ BILL SUMMARY ------
Total Quantity: 25
Initial Grand Total: Rs. 2000.0
No 10% Discount Applied
5% Quantity Discount Applied: -Rs. 100.0
No Membership Discount Applied
Final Payable Amount: Rs. 1900.0


## Test Case 4: Only 2% membership discount applied
**Input:**
2
G707
Mouse
2
2000
H808
Keyboard
1
3000


**Output:**
Enter number of items: 2

Enter details for Item 1
Item code: G707
Description: Mouse
Quantity: 2
Price per item: 2000
Item Total: Rs. 4000.0

Enter details for Item 2
Item code: H808
Description: Keyboard
Quantity: 1
Price per item: 3000
Item Total: Rs. 3000.0

------ BILL SUMMARY ------
Total Quantity: 3
Initial Grand Total: Rs. 7000.0
No 10% Discount Applied
No Quantity Discount Applied
2% Membership Discount Applied: -Rs. 140.0
Final Payable Amount: Rs. 6860.0


## Test Case 5: Both 10% and 5% discounts applied, no membership
**Input:**
3
I909
Laptop
10
800
J010
Mousepad
15
200
K111
Monitor
5
1000
n


**Output:**
Enter number of items: 3

Enter details for Item 1
Item code: I909
Description: Laptop
Quantity: 10
Price per item: 800
Item Total: Rs. 8000.0

Enter details for Item 2
Item code: J010
Description: Mousepad
Quantity: 15
Price per item: 200
Item Total: Rs. 3000.0

Enter details for Item 3
Item code: K111
Description: Monitor
Quantity: 5
Price per item: 1000
Item Total: Rs. 5000.0

------ BILL SUMMARY ------
Total Quantity: 30
Initial Grand Total: Rs. 16000.0
10% Discount Applied: -Rs. 1600.0
5% Quantity Discount Applied: -Rs. 720.0
No Membership Discount Applied
Final Payable Amount: Rs. 13680.0

## Test Case 6: All discounts applied
**Input:**
3
L212
Chair
10
800
M313
Desk
15
1200
N414
Lamp
5
1000

**Output:**
Enter number of items: 3

Enter details for Item 1
Item code: L212
Description: Chair
Quantity: 10
Price per item: 800
Item Total: Rs. 8000.0

Enter details for Item 2
Item code: M313
Description: Desk
Quantity: 15
Price per item: 1200
Item Total: Rs. 18000.0

Enter details for Item 3
Item code: N414
Description: Lamp
Quantity: 5
Price per item: 1000
Item Total: Rs. 5000.0

------ BILL SUMMARY ------
Total Quantity: 30
Initial Grand Total: Rs. 31000.0
10% Discount Applied: -Rs. 3100.0
5% Quantity Discount Applied: -Rs. 1395.0
2% Membership Discount Applied: -Rs. 574.1
Final Payable Amount: Rs. 27030.9