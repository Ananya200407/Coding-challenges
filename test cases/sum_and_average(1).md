# sum_and_average(1).py – Test Cases

## TC1: Normal positive integers
Input:
```
10
20
```
Output:
```
Sum = 30
Average = 15.0
```

## TC2: Decimal values
Input:
```
5.5
2.5
```
Output:
```
Sum = 8.0
Average = 4.0
```

## TC3: One positive and one negative
Input:
```
10
-4
```
Output:
```
Sum = 6
Average = 3.0
```

## TC4: Both negative numbers
Input:
```
-8
-2
```
Output:
```
Sum = -10
Average = -5.0
```

## TC5: Zero values (edge case)
Input:
```
0
0
```
Output:
```
Sum = 0
Average = 0.0
```

## TC6: Very large numbers (edge case)
Input:
```
1000000000
1000000000
```
Output:
```
Sum = 2000000000
Average = 1000000000.0
```

## TC7: Alphabet input (invalid)
Input:
```
abc
10
```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC8: Special characters (invalid)
Input:
```
@#
5
```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC9: Empty input (edge case)
Input:
```

```
Output:
```
Invalid input! Please enter numeric values only.
```

## TC10: Mixed valid and invalid input
Input:
```
5
ten
```
Output:
```
Invalid input! Please enter numeric values only.
```
