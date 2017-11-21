#!usr/bin/python3

"""
Write a program that prints a right-aligned staircase
composed of # symbols and spaces with a height and width of
size n.

Sample Input:
6

Sample Output:
     #
    ##
   ###
  ####
 #####
######
"""


n = 6
for i in range(1, n + 1):
    print(" " * (n - i) + "#" * i)
