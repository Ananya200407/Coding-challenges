# discount(3).py – Test Cases

## TC1: Normal discount
Input:
```
1000
10
```
Output:
```
Discount Amount = 100.0
Final Amount to Pay = 900.0
```

## TC2: Decimal values
Input:
```
2500.50
12.5
```
Output:
```
Discount Amount = 312.5625
Final Amount to Pay = 2187.9375
```

## TC3: Zero discount (edge case)
Input:
```
1500
0
```
Output:
```
Discount Amount = 0.0
Final Amount to Pay = 1500.0
```

## TC4: Zero total amount (edge case)
Input:
```
0
10
```
Output:
```
Discount Amount = 0.0
Final Amount to Pay = 0.0
```

## TC5: 100% discount (edge case)
Input:
```
1000
100
```
Output:
```
Discount Amount = 1000.0
Final Amount to Pay = 0.0
```

## TC6: Very large total amount (edge case)
Input:
```
10000000
20
```
Output:
```
Discount Amount = 2000000.0
Final Amount to Pay = 8000000.0
```

## TC7: Negative total amount (invalid)
Input:
```
-1000
10
```
Output:
```
Total amount and discount percentage must be non-negative.
```

## TC8: Negative discount percentage (invalid)
Input:
```
1000
-5
```
Output:
```
Total amount and discount percentage must be non-negative.
```

## TC9: Discount percentage greater than 100 (invalid)
Input:
```
1000
150
```
Output:
```
Discount percentage cannot exceed 100%.
```

## TC10: Alphabet input (invalid)
Input:
```
abc
10
```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC11: Special characters (invalid)
Input:
```
@#
5
```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC12: Mixed valid and invalid input
Input:
```
1000
ten
```
Output:
```
Invalid input! Please enter numeric values only.
```
