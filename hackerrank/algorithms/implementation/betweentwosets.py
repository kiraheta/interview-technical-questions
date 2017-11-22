#!usr/bin/python3

"""
Given A and B, find and print the number of integers (i.e.,
possible x's) that are between the two sets.

Sample Input:
2 3
2 4
16 32 96

Sample Output:
3
"""


def getTotalX(a, b):
    beg = max(a)
    end = min(b)
    inbetween = 0
    for x in range(beg, end + 1):
        for ai in a:
            if x % ai != 0:
                break
        else:
            for bi in b:
                if bi % x != 0:
                    break
            else:
                inbetween += 1
    return inbetween


if __name__ == "__main__":
    n, m = 2, 3
    a = [2, 4]
    b = [16, 32, 96]
    total = getTotalX(a, b)
    print(total)
