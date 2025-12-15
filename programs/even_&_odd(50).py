n = int(input("Enter number of elements: "))

if n <= 0:
    print("Array size must be greater than 0.")
else:
    arr = []

    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)
