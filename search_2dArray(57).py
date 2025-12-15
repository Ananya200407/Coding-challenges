def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

rows = int(get_numeric_input("Enter number of rows: "))
cols = int(get_numeric_input("Enter number of columns: "))

if rows <= 0 or cols <= 0:
    print("Rows and columns must be greater than 0.")
else:
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            element = get_numeric_input(f"Enter element at position ({i+1},{j+1}): ")
            row.append(element)
        matrix.append(row)


    search_element = get_numeric_input("Enter element to search: ")

    positions = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == search_element:
                positions.append((i+1, j+1))  

    # Display results
    if positions:
        print(f"Element {search_element} found at positions:")
        for pos in positions:
            print(f"Row {pos[0]}, Column {pos[1]}")
    else:
        print(f"Element {search_element} not found in the 2D array.")
