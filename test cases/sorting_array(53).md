Test Case 1: Ascending order

Input:

Enter number of elements: 5
Enter element 1: 4.5
Enter element 2: 2.1
Enter element 3: 9.0
Enter element 4: 1.3
Enter element 5: 6.8
Sort order (asc/desc): asc


Output:

Original array: [4.5, 2.1, 9.0, 1.3, 6.8]
Sorted array (ascending): [1.3, 2.1, 4.5, 6.8, 9.0]

Test Case 2: Descending order

Input:

Enter number of elements: 4
Enter element 1: 10
Enter element 2: 5
Enter element 3: 20
Enter element 4: 15
Sort order (asc/desc): desc


Output:

Original array: [10.0, 5.0, 20.0, 15.0]
Sorted array (descending): [20.0, 15.0, 10.0, 5.0]

Test Case 3: Single element

Input:

Enter number of elements: 1
Enter element 1: 7.5
Sort order (asc/desc): asc


Output:

Original array: [7.5]
Sorted array (ascending): [7.5]

Test Case 4: Already sorted input

Input:

Enter number of elements: 4
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter element 4: 4
Sort order (asc/desc): asc


Output:

Original array: [1.0, 2.0, 3.0, 4.0]
Sorted array (ascending): [1.0, 2.0, 3.0, 4.0]

Test Case 5: Duplicate elements

Input:

Enter number of elements: 5
Enter element 1: 3
Enter element 2: 1
Enter element 3: 3
Enter element 4: 2
Enter element 5: 1
Sort order (asc/desc): desc


Output:

Original array: [3.0, 1.0, 3.0, 2.0, 1.0]
Sorted array (descending): [3.0, 3.0, 2.0, 1.0, 1.0]

Test Case 6: Invalid sort order

Input:

Enter number of elements: 3
Enter element 1: 5
Enter element 2: 2
Enter element 3: 8
Sort order (asc/desc): up


Output:

Original array: [5.0, 2.0, 8.0]
Invalid sort order! Please enter 'asc' or 'desc'.