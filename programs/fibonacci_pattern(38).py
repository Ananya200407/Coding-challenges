n = int(input("Enter number of rows: "))

if n <= 0:
    print("Number of rows must be greater than 0.")
else:
    a, b = 1, 1  
    for i in range(1, n + 1): 
        for j in range(i):  
            print(a, end=" ")
            a, b = b, a + b
        print()
