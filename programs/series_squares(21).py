try:
    N = int(input("Enter the maximum value N: "))

    if N < 1:
        print("No terms in the series for N <", N)
    else:
        print("Series up to", N, "is:")
        num = 1
        while num**2 <= N:
            if num != 4:
                print(num**2, end=", " if (num+1)**2 <= N else "\n")
            num += 1

except ValueError:
    print("Invalid input! Please enter a positive integer.")
