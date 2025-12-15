try:
    N = int(input("Enter the maximum value N: "))

    if N < 1:
        print("No terms in the series for N <", N)
    else:
        print("Fibonacci series up to", N, "is:")
        a, b = 1, 1

        while a <= N:
            print(a, end=", " if a + b <= N else "\n")
            a, b = b, a + b

except ValueError:
    print("Invalid input! Please enter a positive integer.")
