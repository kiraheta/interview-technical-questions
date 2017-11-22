#!usr/bin/python3

"""
Given the value of d for m apples and n oranges, can you determine
how many apples and oranges will fall on Sam's house (i.e., in
the inclusive range [s,t])? Print the number of apples that fall
on Sam's house as your first line of output, then print the number
of oranges that fall on Sam's house as your second line of output.

Sample Input:
7 11
5 15
3 2
-2 2 1
5 -6

Sample Output:
1
1
"""


def apple_and_orange(s, t, a, b, m, n, apple, orange):
    apples = oranges = 0
    for i in range(len(apple)):
        diff = a + apple[i]
        if s <= diff <= t:
            apples += 1
    for j in range(len(orange)):
        diff = b + orange[j]
        if s <= diff <= t:
            oranges += 1
    return (apples, oranges)


if __name__ == '__main__':
    s, t = 7, 11
    a, b = 5, 15
    m, n = 3, 2
    apple = [-2, 2, 1]
    orange = [5, -6]

    apples, oranges = apple_and_orange(s, t, a, b, m, n, apple, orange)
    print(apples)
    print(oranges)
