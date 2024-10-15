"""
 Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
"""
def min_of_tuples(n):
    values = []
    for _ in range(n):
        value = int(input())
        values.append(value)
    return min(values)
n = int(input())
result = min_of_tuples(n)
print(result)
