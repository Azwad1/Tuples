"""
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
"""
input_elements = input("Enter tuple elements separated by spaces:\n")
elements_tuple = tuple(input_elements.split())
print(len(elements_tuple))
