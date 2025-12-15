num = input("Enter a decimal number: ")

try:
    num = float(num)

    whole = int(num)

    fraction = num - whole

    print("Whole part:", whole)
    print("Fractional part:", round(fraction, 6))  

except ValueError:
    print("Invalid input! Please enter a valid decimal number.")
