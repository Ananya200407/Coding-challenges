# Accept the size of the array
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []

    # Accept elements
    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        arr.append(element)

    # Calculate sum
    total = sum(arr)

    print("Array elements:", arr)
    print("Sum of all elements:", total)
