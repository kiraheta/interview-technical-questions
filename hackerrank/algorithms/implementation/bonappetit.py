#!usr/bin/python3

"""
Given n, k the cost of each of the n items, and the total amount
of money that Brian charged Anna for her portion of the bill. If
the bill is fairly split, print Bon Appetit; otherwise, print the
amount of money that Brian must refund to Anna.

Sample Input:
4 1
3 10 2 9
12

Sample Output:
5
"""

def bonAppetit(n, k, b, ar):
    actual = (sum(ar) - ar[k]) // 2
    if b == actual:
        result = "Bon Appetit"
    else:
        diff = b - actual
        result = diff
    return result

if __name__ == '__main__':
    n, k = 4, 1
    ar = [3, 10, 2, 9]
    b = 12
    result = bonAppetit(n, k, b, ar)
    print(result)
