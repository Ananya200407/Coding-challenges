import math

n = int(input("Enter number of rows: "))

if n <= 0:
    print("Number of rows must be greater than 0.")
else:
    current_number = 1  # Start from 1
    for i in range(1, n + 1):  # For each row
        row_numbers = []
        for j in range(i):  # Numbers in current row
            fact = math.factorial(current_number)
            row_numbers.append(str(fact))
            current_number += 1
        print(" ".join(row_numbers))
