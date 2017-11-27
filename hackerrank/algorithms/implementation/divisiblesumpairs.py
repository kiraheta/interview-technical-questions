#!usr/bin/python3

"""
Given an array of n integers, a0, a1,...an-1 and a positive
integer k, find and print the number of (i, j) pairs where
i < j  and ai + aj is divisible by k.

Sample Input:
6 3
1 3 2 6 1 2

Sample Output:
5
"""


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    n, k = 6, 3
    ar = [1, 3, 2, 6, 1, 2]
    result = divisibleSumPairs(n, k, ar)
    print(result)
