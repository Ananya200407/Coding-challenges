Test Case 1: Valid Square Matrices (2 × 2)

Input:

Enter number of rows of Matrix A: 2
Enter number of columns of Matrix A: 2
Enter number of rows of Matrix B: 2
Enter number of columns of Matrix B: 2

Enter elements of Matrix A:
A[1][1]: 1
A[1][2]: 2
A[2][1]: 3
A[2][2]: 4

Enter elements of Matrix B:
B[1][1]: 5
B[1][2]: 6
B[2][1]: 7
B[2][2]: 8


Output:

Resultant Matrix:
19 22
43 50

Test Case 2: Rectangular Matrices (2 × 3) × (3 × 2)

Input:

Enter number of rows of Matrix A: 2
Enter number of columns of Matrix A: 3
Enter number of rows of Matrix B: 3
Enter number of columns of Matrix B: 2

Enter elements of Matrix A:
A[1][1]: 1
A[1][2]: 2
A[1][3]: 3
A[2][1]: 4
A[2][2]: 5
A[2][3]: 6

Enter elements of Matrix B:
B[1][1]: 7
B[1][2]: 8
B[2][1]: 9
B[2][2]: 10
B[3][1]: 11
B[3][2]: 12


Output:

Resultant Matrix:
58 64
139 154

Test Case 3: Single Row × Single Column (1 × 3) × (3 × 1)

Input:

Enter number of rows of Matrix A: 1
Enter number of columns of Matrix A: 3
Enter number of rows of Matrix B: 3
Enter number of columns of Matrix B: 1

Enter elements of Matrix A:
A[1][1]: 2
A[1][2]: 3
A[1][3]: 4

Enter elements of Matrix B:
B[1][1]: 5
B[2][1]: 6
B[3][1]: 7


Output:

Resultant Matrix:
56

Test Case 4: Identity Matrix Multiplication (3 × 3)

Input:

Enter number of rows of Matrix A: 3
Enter number of columns of Matrix A: 3
Enter number of rows of Matrix B: 3
Enter number of columns of Matrix B: 3

Enter elements of Matrix A:
A[1][1]: 1
A[1][2]: 0
A[1][3]: 0
A[2][1]: 0
A[2][2]: 1
A[2][3]: 0
A[3][1]: 0
A[3][2]: 0
A[3][3]: 1

Enter elements of Matrix B:
B[1][1]: 9
B[1][2]: 8
B[1][3]: 7
B[2][1]: 6
B[2][2]: 5
B[2][3]: 4
B[3][1]: 3
B[3][2]: 2
B[3][3]: 1


Output:

Resultant Matrix:
9 8 7
6 5 4
3 2 1

Test Case 5: Incompatible Matrix Sizes

Input:

Enter number of rows of Matrix A: 2
Enter number of columns of Matrix A: 3
Enter number of rows of Matrix B: 2
Enter number of columns of Matrix B: 2


Output:

Error! Number of columns of Matrix A must equal number of rows of Matrix B.

Test Case 6: Zero Matrix Multiplication

Input:

Enter number of rows of Matrix A: 2
Enter number of columns of Matrix A: 2
Enter number of rows of Matrix B: 2
Enter number of columns of Matrix B: 2

Enter elements of Matrix A:
A[1][1]: 0
A[1][2]: 0
A[2][1]: 0
A[2][2]: 0

Enter elements of Matrix B:
B[1][1]: 5
B[1][2]: 6
B[2][1]: 7
B[2][2]: 8


Output:

Resultant Matrix:
0 0
0 0
