try:
    N = int(input("Enter the maximum value N: "))

    if N < 1:
        print("No terms in the series for N <", N)
    else:
        print("Series up to", N, "is:")
        term = 1
        increment = 1

        while term <= N:
            print(term, end=", " if term + increment + 1 <= N else "\n")
            term += increment
            increment += 1

except ValueError:
    print("Invalid input! Please enter a positive integer.")
