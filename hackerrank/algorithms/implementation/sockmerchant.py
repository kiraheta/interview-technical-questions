#!usr/bin/python3

"""
Given n and the color of each sock, how many pairs of socks can
John sell?

Sample Input:
9
10 20 20 10 10 30 50 10 20

Sample Output:
3
"""


def solve(arr):
    pairs = {}
    count = 0
    for item in arr:
        if item in pairs.keys():
            pairs[item] += 1
        else:
            pairs[item] = 1
    for k, v in pairs.items():
        if v >= 2:
            count += v // 2
    return count


if __name__ == '__main__':
    arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = solve(arr)
    print(result)
