n = int(input("Enter number of terms: "))

if n <= 0:
    print("Number of terms must be greater than 0.")
else:
    current = 1
    for i in range(n):
        print(current, end=", " if i < n-1 else "\n")
        current = -current - 4 if current > 0 else -current + 4
