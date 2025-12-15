n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []
    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        arr.append(element)

    maximum = max(arr)

    print("Array elements:", arr)
    print("Maximum value in the array:", maximum)
