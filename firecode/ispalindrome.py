#!/bin/usr/python

"""
A palindrome is a string or sequence of characters that reads the same backward 
and forward. For example, "madam" is a palindrome.
Write a function that takes in a string and returns a Boolean -> True if the 
input string is a palindrome and False
if it is not. An empty string is considered a palindrome. You also need to 
account for the space character. For example, "race car" should return False 
as read backward it is "rac ecar".

Examples:
is_palindrome("madam") -> True

is_palindrome("aabb") -> False

is_palindrome("race car") -> False

is_palindrome("") -> True
"""


def is_palindrome(input_string):
    reverse = input_string[::-1]
    if input_string == reverse:
        return True
    else:
        return False


def is_palindrome(input_string):
    return input_string == input_string[::-1]


if __name__ == '__main__':
    a_str = "race car"
    print(is_palindrome(a_str))
