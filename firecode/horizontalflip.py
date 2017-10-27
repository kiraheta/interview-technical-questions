#!/usr/bin/python

"""  
You are given an m x n 2D image matrix (List of Lists) where each integer 
represents a pixel. Flip it in-place along its horizontal axis.

Example:

Input image :  
              1 1
              0 0
Modified to :   
              0 0
              1 1
"""


def flip_horizontal_axis(matrix):
    size = len(matrix)
    for i in range(size // 2):
        matrix[i], matrix[size - 1 - i] = matrix[size - 1 - i], matrix[i]
    return matrix


def flip_horizontal_axis(matrix):
    matrix.reverse()
    return matrix


if __name__ == '__main__':
    matrix = [[1, 1], [0, 0]]
    print(flip_horizontal_axis(matrix))
