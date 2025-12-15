def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


try:
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time (in years): "))

    if p < 0 or r < 0 or t < 0:
        print("Principal, rate, and time must be non-negative values.")
    else:
        si = calculate_simple_interest(p, r, t)
        print("Simple Interest =", si)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
