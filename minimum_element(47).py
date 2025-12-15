n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []

    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        arr.append(element)

    minimum = min(arr)

    print("Array elements:", arr)
    print("Minimum value in the array:", minimum)
