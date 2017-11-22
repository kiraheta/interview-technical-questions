#!usr/bin/python3

"""
Given the starting locations and movement rates for each kangaroo,
determine if they'll ever land at the same location at the same
time.

Print YES if they can land on the same location at the same time;
otherwise, print NO.

Sample Input:
0 3 4 2

Sample Output:
YES
"""


def kangaroo(x1, v1, x2, v2):
    same_location = " "
    if 0 <= x1 <= 10000 and 0 <= x2 <= 10000:
        if x1 == x2 and v1 == v2:
            same_location = "YES"
        elif (x1 == x2 and v1 > v2) or (x1 <= x2 and v1 <= v2):
            same_location = "NO"
        else:
            if ((x2 - x1) % (v1 - v2)) == 0:
                same_location = "YES"
            else:
                same_location = "NO"
    return same_location


if __name__ == '__main__':
    x1, v1, x2, v2 = 0, 3, 4, 2
    result = kangaroo(x1, v1, x2, v2)
    print(result)
