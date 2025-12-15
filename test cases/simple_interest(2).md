# simple_interest(2).py – Test Cases

## TC1: Normal values
Input:
```
1000
5
2
```
Output:
```
Simple Interest = 100.0
```

## TC2: Decimal values
Input:
```
2500.5
3.5
1.5
```
Output:
```
Simple Interest = 131.27625
```

## TC3: Zero principal (edge case)
Input:
```
0
5
2
```
Output:
```
Simple Interest = 0.0
```

## TC4: Zero rate of interest (edge case)
Input:
```
1000
0
3
```
Output:
```
Simple Interest = 0.0
```

## TC5: Zero time period (edge case)
Input:
```
1000
5
0
```
Output:
```
Simple Interest = 0.0
```

## TC6: Very large values (edge case)
Input:
```
10000000
10
5
```
Output:
```
Simple Interest = 5000000.0
```

## TC7: Negative principal (invalid)
Input:
```
-1000
5
2
```
Output:
```
Principal, rate, and time must be non-negative values.
```

## TC8: Negative rate (invalid)
Input:
```
1000
-5
2
```
Output:
```
Principal, rate, and time must be non-negative values.
```

## TC9: Negative time (invalid)
Input:
```
1000
5
-2
```
Output:
```
Principal, rate, and time must be non-negative values.
```

## TC10: Alphabet input (invalid)
Input:
```
abc
5
2
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
2
```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC12: Mixed valid and invalid input
Input:
```
1000
five
2
```
Output:
```
Invalid input! Please enter numeric values only.
```
