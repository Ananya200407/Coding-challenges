try:
    N = int(input("Enter the maximum value N: "))

    if N < 1:
        print("No terms in the series for N <", N)
    else:
        print("Series up to", N, "is:")
        series = [1]  
        while True:
            if len(series) == 1:
                next_term = series[-1] + 3
            elif len(series) == 2:
                next_term = series[-1] + 3
            elif len(series) == 3:
                next_term = series[-1] + 5
            elif len(series) == 4:
                next_term = series[-1] + 11
            else:
                next_term = series[-1] + (series[-1] - series[-2])*2

            if next_term > N:
                break
            series.append(next_term)

        print(", ".join(str(x) for x in series))

except ValueError:
    print("Invalid input! Please enter a positive integer.")
