n = int(input("Enter number of rows: "))

if n <= 0:
    print("Number of rows must be greater than 0.")
else:
    for i in range(1, n + 1):
        print(str(i) * 5)
