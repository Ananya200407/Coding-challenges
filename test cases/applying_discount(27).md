# Test Cases for Multiple Item Billing with Discounts



## Test Case 1: Total < 10000, quantity ≤ 20 (No discount)
**Input:**
- Number of items: 2  
- Item 1: Code A101, Desc Pen, Quantity 5, Price 100  
- Item 2: Code B202, Desc Notebook, Quantity 10, Price 200  

**Expected Output:**
Item Total: Rs. 500.0
Item Total: Rs. 2000.0

------ BILL SUMMARY ------
Total Quantity: 15
Initial Grand Total: Rs. 2500.0
No 10% Discount Applied
No Quantity Discount Applied
Final Payable Amount: Rs. 2500.0


## Test Case 2: Total > 10000, quantity ≤ 20 (10% discount only)
**Input:**
- Number of items: 2  
- Item 1: Code C303, Desc Chair, Quantity 10, Price 800  
- Item 2: Code D404, Desc Table, Quantity 5, Price 1200  

**Expected Output:**
Item Total: Rs. 8000.0
Item Total: Rs. 6000.0

------ BILL SUMMARY ------
Total Quantity: 15
Initial Grand Total: Rs. 14000.0
10% Discount Applied: -Rs. 1400.0
No Quantity Discount Applied
Final Payable Amount: Rs. 12600.0


## Test Case 3: Total < 10000, quantity > 20 (5% quantity discount only)
**Input:**
- Number of items: 2  
- Item 1: Code E505, Desc Pen, Quantity 15, Price 100  
- Item 2: Code F606, Desc Notebook, Quantity 10, Price 50  

**Expected Output:**
Item Total: Rs. 1500.0
Item Total: Rs. 500.0

------ BILL SUMMARY ------
Total Quantity: 25
Initial Grand Total: Rs. 2000.0
No 10% Discount Applied
Additional 5% Quantity Discount Applied: -Rs. 100.0
Final Payable Amount: Rs. 1900.0


## Test Case 4: Total > 10000, quantity > 20 (Both discounts applied)
**Input:**
- Number of items: 3  
- Item 1: Code G707, Desc Laptop, Quantity 10, Price 800  
- Item 2: Code H808, Desc Mouse, Quantity 15, Price 200  
- Item 3: Code I909, Desc Keyboard, Quantity 5, Price 100  

**Expected Output:**
Item Total: Rs. 8000.0
Item Total: Rs. 3000.0
Item Total: Rs. 500.0

------ BILL SUMMARY ------
Total Quantity: 30
Initial Grand Total: Rs. 11500.0
10% Discount Applied: -Rs. 1150.0
Additional 5% Quantity Discount Applied: -Rs. 517.5
Final Payable Amount: Rs. 9877.5


## Test Case 5: Negative quantity or price (Item skipped)
**Input:**
- Number of items: 2  
- Item 1: Code J010, Desc Ruler, Quantity -2, Price 20  
- Item 2: Code K111, Desc Eraser, Quantity 5, Price -10  

**Expected Output:**
- Quantity and price must be non-negative. Item skipped.  
------ BILL SUMMARY ------
Total Quantity: 0
Initial Grand Total: Rs. 0.0
No 10% Discount Applied
No Quantity Discount Applied
Final Payable Amount: Rs. 0.0


## Test Case 6: Mixed valid and invalid items
**Input:**
- Number of items: 3  
- Item 1: Code L212, Desc Pen Stand, Quantity 5, Price 500  
- Item 2: Code M313, Desc Chair, Quantity -1, Price 200  
- Item 3: Code N414, Desc Table, Quantity 10, Price 100  

**Expected Output:**
Item Total: Rs. 2500.0
Quantity and price must be non-negative. Item skipped.
Item Total: Rs. 1000.0

------ BILL SUMMARY ------
Total Quantity: 15
Initial Grand Total: Rs. 3500.0
No 10% Discount Applied
No Quantity Discount Applied
Final Payable Amount: Rs. 3500.0


## Test Case 7: Non-numeric input
**Input:**
- Number of items: abc  

**Expected Output:**
- Invalid input! Please enter numeric values correctly.