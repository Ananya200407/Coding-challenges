try:
    # Input from user
    num = int(input("Enter an integer: "))

    # Check even or odd
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
