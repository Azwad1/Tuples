"""
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
"""
def sum_of_tuple_elements(values):
    tuple_values = tuple(map(int, values.split()))
    total_sum = 0
    for value in tuple_values:
        total_sum += value
    return total_sum
values = input()
result = sum_of_tuple_elements(values)
print(result)
