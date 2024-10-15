"""
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
"""
def count_and_factorial(values, x):
    tuple_values = tuple(map(int, values.split()))
    count_x = tuple_values.count(x)
    factorial = 1
    for i in range(1, count_x + 1):
        factorial *= i
    return factorial
values = input()
x = int(input())
result = count_and_factorial(values, x)
print(result)
