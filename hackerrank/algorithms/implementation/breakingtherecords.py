#!usr/bin/python3

"""
Given Maria's array of scores for a season of n games, find and
print the number of times she breaks her record for most and
least points scored during the season.

Sample Input:
9
10 5 20 20 4 5 2 25 1

Sample Output:
2 4
"""


def getRecord(s):
    min_score = max_score = s[0]
    min_count = max_count = 0
    for score in s:
        if min_score < score:
            min_score = score
            min_count += 1
        if max_score > score:
            max_score = score
            max_count += 1
    return (min_count, max_count)


n = 9
s = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result = getRecord(s)
print(" ".join(map(str, result)))
