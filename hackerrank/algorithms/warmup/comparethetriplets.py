#!usr/bin/python3

"""
Given A and B, where A = (a0, a1, a2) and B = (b0, b1, b2), write a function to
return the comparison points, total points a person earned, as two
space-separated integers between Alice and Bob.

Sample Input:
5 6 7
3 6 10

Sample Output:
1 1
"""


def solve(a0, a1, a2, b0, b1, b2):
    alice_bob_count = [0, 0]
    compare(alice_bob_count, a0, b0)
    compare(alice_bob_count, a1, b1)
    compare(alice_bob_count, a2, b2)
    return alice_bob_count


def compare(lst, x, y):
    if x > y:
        lst[0] += 1
    if x < y:
        lst[1] += 1
    return lst


if __name__ == '__main__':

    a0, a1, a2 = 5, 6, 7
    a0, a1, a2 = [int(a0), int(a1), int(a2)]
    b0, b1, b2 = 3, 6, 10
    b0, b1, b2 = [int(b0), int(b1), int(b2)]
    result = solve(a0, a1, a2, b0, b1, b2)
    print(" ".join(map(str, result)))
