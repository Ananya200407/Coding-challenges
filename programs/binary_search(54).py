n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []

    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        arr.append(element)

    print("Original array:", arr)

    arr.sort()
    print("Sorted array for binary search:", arr)

    target = float(input("Enter element to search: "))

    # Binary search implementation
    left = 0
    right = n - 1
    found = False

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"Element {target} found at position {mid + 1}")
            found = True
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if not found:
        print(f"Element {target} not found in the array")
