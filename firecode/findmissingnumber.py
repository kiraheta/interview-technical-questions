#!/usr/bin/python

"""
Given an list containing 9 numbers ranging from 1 to 10, write a function to
find the missing number. Assume you have 9 numbers between 1 to 10 and only
one number is missing.

Example:
input_list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
find_missing_number(input_list) => 3
"""


def find_missing_number(list_numbers):
    for num in list_numbers:
        if num + 1 != list_numbers[num]:
            return num + 1


def find_missing_number(list_numbers):
    return [i for i in range(1, 10) if i not in list_numbers][0]


def find_missing_number(list_numbers):
    return sum(range(11)) - sum(list_numbers)


if __name__ == '__main__':
    lst = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    print(find_missing_number(lst))
