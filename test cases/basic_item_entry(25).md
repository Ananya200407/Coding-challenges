# Test Cases for Item Billing Program

---

## Test Case 1: Valid input
**Input:**
- Item code: A101  
- Description: Pen  
- Quantity: 5  
- Price per item: 10.5  

**Expected Output:**
--- Item Bill Details ---
Item Code: A101
Description: Pen
Quantity: 5
Price per Item: Rs. 10.5
Total Cost: Rs. 52.5


---

## Test Case 2: Quantity = 0
**Input:**
- Item code: B202  
- Description: Notebook  
- Quantity: 0  
- Price per item: 25  

**Expected Output:**
--- Item Bill Details ---
Item Code: B202
Description: Notebook
Quantity: 0
Price per Item: Rs. 25.0
Total Cost: Rs. 0.0


---

## Test Case 3: Price = 0
**Input:**
- Item code: C303  
- Description: Eraser  
- Quantity: 10  
- Price per item: 0  

**Expected Output:**
--- Item Bill Details ---
Item Code: C303
Description: Eraser
Quantity: 10
Price per Item: Rs. 0.0
Total Cost: Rs. 0.0


---

## Test Case 4: Negative quantity
**Input:**
- Item code: D404  
- Description: Sharpener  
- Quantity: -2  
- Price per item: 5  

**Expected Output:**
- Quantity and price must be non-negative values.

---

## Test Case 5: Negative price
**Input:**
- Item code: E505  
- Description: Marker  
- Quantity: 3  
- Price per item: -15  

**Expected Output:**
- Quantity and price must be non-negative values.

---

## Test Case 6: Non-numeric quantity
**Input:**
- Item code: F606  
- Description: Ruler  
- Quantity: abc  
- Price per item: 12  

**Expected Output:**
- Invalid input! Please enter numeric values for quantity and price.

---

## Test Case 7: Large quantity and price
**Input:**
- Item code: I909  
- Description: Laptop  
- Quantity: 1000  
- Price per item: 55000  

**Expected Output:**
--- Item Bill Details ---
Item Code: I909
Description: Laptop
Quantity: 1000
Price per Item: Rs. 55000.0
Total Cost: Rs. 55000000.0