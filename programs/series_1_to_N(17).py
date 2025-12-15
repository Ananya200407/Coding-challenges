try:
    N = int(input("Enter a positive integer N: "))

    if N <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        print("Series up to", N, "is:")
        for i in range(1, N + 1):
            print(i, end=", " if i != N else "\n") 

except ValueError:
    print("Invalid input! Please enter an integer value.")
