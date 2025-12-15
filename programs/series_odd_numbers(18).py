try:
   
    N = int(input("Enter a positive integer N: "))

    if N <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        print("Odd number series up to", N, "is:")
        for i in range(1, N + 1, 2):  
            print(i, end=", " if i + 2 <= N else "\n")

except ValueError:
    print("Invalid input! Please enter an integer value.")
