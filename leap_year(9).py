try:
    year = int(input("Enter a year: "))

    if year <= 0:
        print("Invalid year! Please enter a positive integer.")
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")

except ValueError:
    print("Invalid input! Please enter a valid integer for the year.")
