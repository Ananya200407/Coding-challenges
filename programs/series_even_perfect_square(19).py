try:
    N = int(input("Enter a positive integer N: "))

    if N < 4:
        print("There are no numbers in the series up to", N)
    else:
        print("Series up to", N, "is:")
        num = 2  
        while num**2 <= N:
            print(num**2, end=", " if (num+2)**2 <= N else "\n")
            num += 2

except ValueError:
    print("Invalid input! Please enter a positive integer.")
