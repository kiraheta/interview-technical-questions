#!/usr/bin/python

"""
Write a function to compute the binary representation of a positive decimal 
integer. The method should return a string.

Example:
dec_to_bin(6) ==> "110"

dec_to_bin(5) ==> "101"
Note : Do not use in-built bin() function.
"""


def dec_to_bin(n):
    if n < 2:
        return str(n)
    else:
        return dec_to_bin(n // 2) + dec_to_bin(n % 2)


if __name__ == '__main__':
    print(dec_to_bin(5))
