#!/usr/bin/python

"""
Problem: Two Sum

Description:

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Time complexity: O(n^2)


def two_sum(aList, target):
    if len(aList) <= 1:
        return aList
    for i in range(0, len(aList) - 1):
        for j in range(1, len(aList)):
            if aList[i] + aList[j] == target:
                return [i, j]
    return [-1, -1]

# Time complexity: O(n)


def two_sum_2(aList, target):
    if len(aList) <= 1:
        return aList
    hash_map = {}
    for x in range(0, len(aList)):
        if target - aList[x] in hash_map:
            return [hash_map.get(target - aList[x]), x]
        else:
            hash_map[aList[x]] = x
    return [-1, -1]


if __name__ == '__main__':
    aList = [2, 7, 11, 15]
    target = 9

print(two_sum_2(aList, target))
