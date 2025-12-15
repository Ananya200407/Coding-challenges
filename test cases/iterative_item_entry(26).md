# Test Cases for Multiple Item Billing Program

---

## Test Case 1: Valid input for multiple items
**Input:**
- Number of items: 2  
- Item 1: Code A101, Desc Pen, Quantity 5, Price 10  
- Item 2: Code B202, Desc Notebook, Quantity 3, Price 25  

**Expected Output:**
Item Total: Rs. 50.0
Item Total: Rs. 75.0

========================
Grand Total: Rs. 125.0


---

## Test Case 2: Single item
**Input:**
- Number of items: 1  
- Item 1: Code C303, Desc Eraser, Quantity 10, Price 5  

**Expected Output:**
Item Total: Rs. 50.0

========================
Grand Total: Rs. 50.0


---

## Test Case 3: Zero quantity
**Input:**
- Number of items: 1  
- Item 1: Code D404, Desc Sharpener, Quantity 0, Price 15  

**Expected Output:**
Item Total: Rs. 0.0

========================
Grand Total: Rs. 0.0


---

## Test Case 4: Zero price
**Input:**
- Number of items: 1  
- Item 1: Code E505, Desc Marker, Quantity 5, Price 0  

**Expected Output:**
Item Total: Rs. 0.0

========================
Grand Total: Rs. 0.0


---

## Test Case 5: Negative quantity or price
**Input:**
- Number of items: 2  
- Item 1: Code F606, Desc Ruler, Quantity -2, Price 12  
- Item 2: Code G707, Desc Calculator, Quantity 3, Price -20  

**Expected Output:**
- Quantity and price must be non-negative. Item skipped. (for both items)  


---

## Test Case 6: Mixed valid and invalid items
**Input:**
- Number of items: 3  
- Item 1: Code H808, Desc Pen Stand, Quantity 2, Price 100  
- Item 2: Code I909, Desc Chair, Quantity -1, Price 500  
- Item 3: Code J010, Desc Table, Quantity 1, Price 200  

**Expected Output:**
Item Total: Rs. 200.0
Quantity and price must be non-negative. Item skipped.
Item Total: Rs. 200.0

========================
Grand Total: Rs. 400.0


---

## Test Case 7: Non-numeric input
**Input:**
- Number of items: abc  

**Expected Output:**
- Invalid input! Please enter numeric values correctly.
