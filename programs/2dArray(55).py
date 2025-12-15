rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

if rows <= 0 or cols <= 0:
    print("Rows and columns must be greater than 0.")
else:
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            element = input(f"Enter element at position ({i+1},{j+1}): ")
            row.append(element)
        matrix.append(row)

    print("\n2D Array (row-wise):")
    for row in matrix:
        print(" ".join(row))