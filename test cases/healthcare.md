# HealWell Care Hospital – Test Cases

---

## Test Case 1: Normal Patient, Single Service

### Input:
Name: Ananya
Age: 25
Gender: Female
Contact: 9876543210

Service Selection:
1
0


### Output:
Subtotal : ₹500.00
Discount Applied : ₹0.00
GST (18%) : ₹90.00
Grand Total : ₹590.00

## Test Case 2: Multiple Services, No Discount

### Input:
Name: Rahul Sharma
Age: 40
Gender: Male
Contact: 9123456789

Service Selection:
2
3
4
0



### Calculation:
- Services: Blood Test (300), Covid Test (800), X-Ray (1500)
- Subtotal = 2600

### Output:
Subtotal : ₹2600.00
Discount Applied : ₹0.00
GST (18%) : ₹468.00
Grand Total : ₹3068.00



## Test Case 3: Senior Citizen Discount Applied

### Input:
Name: Suresh Kumar
Age: 65
Gender: Male
Contact: 9988776655

Service Selection:
5
0



### Calculation:
- Subtotal = 4000
- Senior Discount (10%) = 400
- Amount after discount = 3600
- GST = 648

### Output:
Subtotal : ₹4000.00
Discount Applied : ₹400.00
GST (18%) : ₹648.00
Grand Total : ₹4248.00



## Test Case 4: High Bill Discount (> ₹5000)

### Input:
Name: Priya Mehta
Age: 35
Gender: Female
Contact: 9012345678

Service Selection:
6
0


### Calculation:
- Subtotal = 7000
- High Bill Discount (5%) = 350
- Amount after discount = 6650
- GST = 1197

### Output:
Subtotal : ₹7000.00
Discount Applied : ₹350.00
GST (18%) : ₹1197.00
Grand Total : ₹7847.00



## Test Case 5: Senior Citizen + High Bill Discount

### Input:
Name: Ramesh Patil
Age: 70
Gender: Male
Contact: 9876501234

Service Selection:
5
6
0

### Calculation:
- Subtotal = 4000 + 7000 = 11000
- Senior Discount (10%) = 1100
- Remaining = 9900
- High Bill Discount (5%) = 495
- Total Discount = 1595
- Amount after discount = 9405
- GST = 1692.90

### Output:
Subtotal : ₹11000.00
Discount Applied : ₹1595.00
GST (18%) : ₹1692.90
Grand Total : ₹11097.90



## Test Case 6: Invalid Inputs Handling

### Input:
Name: Ananya123


### Output:
Invalid name! Use alphabets only.

