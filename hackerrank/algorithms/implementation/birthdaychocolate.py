#!usr/bin/python3

"""
Given m, d, and the sequence of integers written on each square
of Lily's chocolate bar, find the different ways that Lily can
break off a piece of chocolate to give to Ron where the sum of m
consecutive squares is equal to d.

Sample Input:
5
1 2 1 3 2
3 2

Sample Output:
2
"""


def solve(n, s, d, m):
    count = 0
    for i in range(n - m + 1):
        count += int(sum(s[i:i + m]) == d)
    return count


if __name__ == '__main__':
    n = 5
    s = [1, 2, 1, 3, 2]
    d, m = 3, 2
    result = solve(n, s, d, m)
    print(result)
