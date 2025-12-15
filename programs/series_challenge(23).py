try:
    N = int(input("Enter the maximum value N: "))

    if N < 1:
        print("No terms in the series for N <", N)
    else:
        print("Series up to", N, "is:")
        series = [1]
        i = 0  

        while True:
            if (i + 1) % 4 == 0:
                increment = 8
            else:
                increment = 4

            next_term = series[-1] + increment
            if next_term > N:
                break

            series.append(next_term)
            i += 1

        print(", ".join(str(x) for x in series))

except ValueError:
    print("Invalid input! Please enter a positive integer.")
