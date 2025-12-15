num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid input! Please enter a positive integer.")
else:
    original = int(num)
    reverse = 0
    temp = original

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10
    print("Original:",original)
    print("Reverse:", reverse)
