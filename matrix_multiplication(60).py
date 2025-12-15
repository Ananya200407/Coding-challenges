def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

rows_a = get_integer_input("Enter number of rows of Matrix A: ")
cols_a = get_integer_input("Enter number of columns of Matrix A: ")

rows_b = get_integer_input("Enter number of rows of Matrix B: ")
cols_b = get_integer_input("Enter number of columns of Matrix B: ")

if cols_a != rows_b:
    print("Error! Number of columns of Matrix A must equal number of rows of Matrix B.")
else:
    print("\nEnter elements of Matrix A:")
    matrix_a = []
    for i in range(rows_a):
        row = []
        for j in range(cols_a):
            row.append(get_integer_input(f"A[{i+1}][{j+1}]: "))
        matrix_a.append(row)

    print("\nEnter elements of Matrix B:")
    matrix_b = []
    for i in range(rows_b):
        row = []
        for j in range(cols_b):
            row.append(get_integer_input(f"B[{i+1}][{j+1}]: "))
        matrix_b.append(row)

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):  # or rows_b
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    print("\nResultant Matrix:")
    for row in result:
        print(" ".join(map(str, row)))
