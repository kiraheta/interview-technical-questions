#!usr/bin/python3

"""
Given five positive integers, find the minimum and maximum values
that can be calculated by summing exactly four of the five
integers. Then print the respective minimum and maximum values as
a single line of two space-separated long integers.

Sample Input:
1 2 3 4 5

Sample Output:
10 14
"""

arr = [1, 2, 3, 4, 5]

min_sum = sum(arr) - max(arr)
max_sum = sum(arr) - min(arr)
print(min_sum, max_sum)
