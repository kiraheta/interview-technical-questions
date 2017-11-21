#!usr/bin/python3

"""
Given an array of integers, calculate which fraction of its
elements are positive, which fraction of its elements are
negative, and which fraction of its elements are zeroes,
respectively. Print the decimal value of each fraction on a new
line.

Sample Input:
6
-4 3 -9 0 4 1  

Sample Output:
0.500000
0.333333
0.166667
"""

if __name__ == '__main__':

    n = 6
    arr = [-4, 3, -9, 0, 4, 1]
    pos_count = neg_count = zer_count = 0
    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zer_count += 1
    print(pos_count / n)
    print(neg_count / n)
    print(zer_count / n)
