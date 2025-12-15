def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

rows = get_integer_input("Enter number of rows: ")
cols = get_integer_input("Enter number of columns: ")

if rows <= 0 or cols <= 0:
    print("Rows and columns must be greater than 0.")
else:
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            element = get_integer_input(f"Enter element at position ({i+1},{j+1}): ")
            row.append(element)
        matrix.append(row)

    print("\nOriginal Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

    transpose = []
    for j in range(cols):
        trans_row = []
        for i in range(rows):
            trans_row.append(matrix[i][j])
        transpose.append(trans_row)

    print("\nTranspose of Matrix:")
    for row in transpose:
        print(" ".join(map(str, row)))
