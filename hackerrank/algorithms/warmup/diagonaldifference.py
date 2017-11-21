#!usr/bin/python3

"""
Given a square matrix of size N X N, calculate the absolute
difference between the sums of its diagonals. Print the
absolute difference between the two sums of the matrix's
diagonals as a single integer.

Sample Input:
3
11 2 4
4 5 6
10 8 -12

Sample Output:
15
"""


import sys


lr_sum = 0
rl_sum = 0
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    lr_sum += a_t[a_i]
    rl_sum += a_t[(n - 1) - a_i]
result = abs(lr_sum - rl_sum)
print(result)
