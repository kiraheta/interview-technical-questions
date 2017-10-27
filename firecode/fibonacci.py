#!bin/usr/python

"""
The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 
34, ... The next number is found by adding up the two numbers before it.

Write a recursive method fib(n) that returns the nth Fibonacci number. n is 0 
indexed, which means that in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., 
n == 0 should return 0 and n == 3 should return 2.
Assume n is less than 15.

Examples:
fib(0) ==> 0

fib(1) ==> 1

fib(3) ==> 2
"""


def fib(n):
    if n <= 1:
        return n
    return (fib(n - 1) + fib(n - 2))


if __name__ == '__main__':
    print(fib(3))
