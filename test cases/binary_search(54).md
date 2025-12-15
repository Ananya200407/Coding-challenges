Test Case 1: Element Found (Middle Position)

Input:

Enter number of elements: 5
Enter element 1: 10
Enter element 2: 5
Enter element 3: 20
Enter element 4: 15
Enter element 5: 25
Enter element to search: 15


Output:

Original array: [10.0, 5.0, 20.0, 15.0, 25.0]
Sorted array for binary search: [5.0, 10.0, 15.0, 20.0, 25.0]
Element 15.0 found at position 3

Test Case 2: Element Found (First Position)

Input:

Enter number of elements: 4
Enter element 1: 8
Enter element 2: 3
Enter element 3: 6
Enter element 4: 1
Enter element to search: 1


Output:

Original array: [8.0, 3.0, 6.0, 1.0]
Sorted array for binary search: [1.0, 3.0, 6.0, 8.0]
Element 1.0 found at position 1

Test Case 3: Element Found (Last Position)

Input:

Enter number of elements: 6
Enter element 1: 12
Enter element 2: 7
Enter element 3: 19
Enter element 4: 3
Enter element 5: 15
Enter element 6: 25
Enter element to search: 25


Output:

Original array: [12.0, 7.0, 19.0, 3.0, 15.0, 25.0]
Sorted array for binary search: [3.0, 7.0, 12.0, 15.0, 19.0, 25.0]
Element 25.0 found at position 6

Test Case 4: Element Not Found

Input:

Enter number of elements: 5
Enter element 1: 2
Enter element 2: 4
Enter element 3: 6
Enter element 4: 8
Enter element 5: 10
Enter element to search: 7


Output:

Original array: [2.0, 4.0, 6.0, 8.0, 10.0]
Sorted array for binary search: [2.0, 4.0, 6.0, 8.0, 10.0]
Element 7.0 not found in the array

Test Case 5: Single Element – Found

Input:

Enter number of elements: 1
Enter element 1: 9
Enter element to search: 9


Output:

Original array: [9.0]
Sorted array for binary search: [9.0]
Element 9.0 found at position 1

Test Case 6: Single Element – Not Found

Input:

Enter number of elements: 1
Enter element 1: 5
Enter element to search: 3


Output:

Original array: [5.0]
Sorted array for binary search: [5.0]
Element 3.0 not found in the array

Test Case 7: Invalid Array Size

Input:

Enter number of elements: 0


Output:

Array size must be greater than 0.