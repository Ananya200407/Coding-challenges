def sum_and_average(a, b):
    total = a + b
    average = total / 2
    return total, average


try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    s, avg = sum_and_average(x, y)

    print("Sum =", s)
    print("Average =", avg)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
