n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []
    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        arr.append(element)

    print("Original array:", arr)

    # Accept sort order
    order = input("Sort order (asc/desc): ").strip().lower()

    if order == "asc":
        sorted_arr = sorted(arr)
        print("Sorted array (ascending):", sorted_arr)
    elif order == "desc":
        sorted_arr = sorted(arr, reverse=True)
        print("Sorted array (descending):", sorted_arr)
    else:
        print("Invalid sort order! Please enter 'asc' or 'desc'.")
