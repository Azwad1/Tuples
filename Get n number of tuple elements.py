"""
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
"""
def sum_of_tuples(n):
    total_sum = 0
    for _ in range(n):
        value = int(input())
        total_sum += value
    return total_sum
n = int(input())
result = sum_of_tuples(n)
print(result)
