n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        arr.append(element)

    search_element = input("Enter element to search: ")

    found = False
    for i in range(n):
        if arr[i] == search_element:
            print(f"Element {search_element} found at position {i+1}")
            found = True
            break

    if not found:
        print(f"Element {search_element} not found in the array")
