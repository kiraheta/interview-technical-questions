#!/usr/bin/python

"""  
Write a function that takes in a string and returns the reversed version of 
the string.

Examples:

reverse_string("abcde") -> "edcba"

reverse_string("1") -> "1"

reverse_string("") -> ""

reverse_string("madam") -> "madam"
"""


def reverse_string(a_string):
    return a_string[::-1]


def reverse_string(a_string):
    str = list(a_string)
    for i in range(len(a_string) // 2):
        str[i], str[-i - 1] = str[-i - 1], str[i]
    return ''.join(str)


if __name__ == '__main__':
    a_string = "carrots"
    print(reverse_string(a_string))
