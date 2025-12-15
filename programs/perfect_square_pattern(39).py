n = int(input("Enter number of rows: "))

if n <= 0:
    print("Number of rows must be greater than 0.")
else:
    current_number = 1  
    for i in range(1, n + 1):  
        row_numbers = []
        for j in range(i):  
            square = current_number ** 2
            if (j + 1) % 2 == 0:  
                square = -square
            row_numbers.append(str(square))
            current_number += 1
        print(" ".join(row_numbers))
