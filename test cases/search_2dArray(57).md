Test Case 1: Element Present Once

Input:

Enter number of rows: 2
Enter number of columns: 3
Enter element at position (1,1): 1
Enter element at position (1,2): 2
Enter element at position (1,3): 3
Enter element at position (2,1): 4
Enter element at position (2,2): 5
Enter element at position (2,3): 6
Enter element to search: 5


Output:

Element 5.0 found at positions:
Row 2, Column 2

Test Case 2: Element Present Multiple Times

Input:

Enter number of rows: 3
Enter number of columns: 3
Enter element at position (1,1): 1
Enter element at position (1,2): 2
Enter element at position (1,3): 3
Enter element at position (2,1): 2
Enter element at position (2,2): 4
Enter element at position (2,3): 5
Enter element at position (3,1): 6
Enter element at position (3,2): 2
Enter element at position (3,3): 7
Enter element to search: 2


Output:

Element 2.0 found at positions:
Row 1, Column 2
Row 2, Column 1
Row 3, Column 2

Test Case 3: Element Not Found

Input:

Enter number of rows: 2
Enter number of columns: 2
Enter element at position (1,1): 10
Enter element at position (1,2): 20
Enter element at position (2,1): 30
Enter element at position (2,2): 40
Enter element to search: 50


Output:

Element 50.0 not found in the 2D array.

Test Case 4: Single Element Matrix – Found

Input:

Enter number of rows: 1
Enter number of columns: 1
Enter element at position (1,1): 9
Enter element to search: 9


Output:

Element 9.0 found at positions:
Row 1, Column 1

Test Case 5: Decimal Values Search

Input:

Enter number of rows: 2
Enter number of columns: 2
Enter element at position (1,1): 1.5
Enter element at position (1,2): 2.5
Enter element at position (2,1): 3.5
Enter element at position (2,2): 4.5
Enter element to search: 2.5


Output:

Element 2.5 found at positions:
Row 1, Column 2

Test Case 6: Invalid Row Input

Input:

Enter number of rows: 0
Enter number of columns: 3


Output:

Rows and columns must be greater than 0