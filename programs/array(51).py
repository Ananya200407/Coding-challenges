n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        arr.append(element)

    print("Array elements:", arr)
