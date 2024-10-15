"""
 Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
"""
def max_of_tuples(n):
    values = []
    for _ in range(n):
        value = int(input())
        values.append(value)
    return max(values)
n = int(input())
result = max_of_tuples(n)
print(result)
