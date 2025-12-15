# swap_two_numbers(4).py – Test Cases

## TC1: Normal positive numbers
Input:
```
10
20
```
Output:
```
After swapping:
a = 20.0
b = 10.0
```

## TC2: Negative numbers
Input:
```
-5
-15
```
Output:
```
After swapping:
a = -15.0
b = -5.0
```

## TC3: One positive, one negative
Input:
```
8
-3
```
Output:
```
After swapping:
a = -3.0
b = 8.0
```

## TC4: Zero and positive number (edge case)
Input:
```
0
25
```
Output:
```
After swapping:
a = 25.0
b = 0.0
```

## TC5: Zero and zero (edge case)
Input:
```
0
0
```
Output:
```
After swapping:
a = 0.0
b = 0.0
```

## TC6: Decimal numbers
Input:
```
3.5
7.2
```
Output:
```
After swapping:
a = 7.2
b = 3.5
```

## TC7: Very large numbers (edge case)
Input:
```
1000000000
-999999999
```
Output:
```
After swapping:
a = -999999999.0
b = 1000000000.0
```

## TC8: Same numbers
Input:
```
5
5
```
Output:
```
After swapping:
a = 5.0
b = 5.0
```

## TC9: Alphabet input (invalid)
Input:
```
abc
10
```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC10: Special characters (invalid)
Input:
```
@
5
```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC11: Mixed valid and invalid input
Input:
```
10
xyz
```
Output:
```
Invalid input! Please enter numeric values only.
```
