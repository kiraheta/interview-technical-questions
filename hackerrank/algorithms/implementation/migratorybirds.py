#!usr/bin/python3

"""
Given an array of n integers where each integer describes the type
of a bird in the flock, find and print the type number of the most
common bird. If two or more types of birds are equally common,
choose the type with the smallest ID number.

Sample Input:
6
1 4 4 4 5 3

Sample Output:
4
"""


def migratoryBirds(n, ar):
    frequency = {}
    max_keys = []
    for item in ar:
        if item in frequency.keys():
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_value = max(frequency.values())
    for k, v in frequency.items():
        if max_value == v:
            max_keys.append(k)
    return min(max_keys)


if __name__ == '__main__':

    n = 6
    ar = [1, 4, 4, 5, 3]
    result = migratoryBirds(n, ar)
    print(result)
