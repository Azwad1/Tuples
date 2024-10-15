"""
 Write a program to get the tuple values in a single line separated by space and count the number of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
"""
def count_value_in_tuple(values, x):
    tuple_values = tuple(map(int, values.split()))
    return tuple_values.count(x)
values = input()
x = int(input())
result = count_value_in_tuple(values, x)
print( result)
