#!/usr/bin/python3
"""Module 0-rotate_2d_matrix
"""

def rotate_2d_matrix(matrix):
    """rotate a matrix by 90 deg
    """
    val = len(matrix)
    temp = create_matrix(val)
    for row in range(val):
        for col in range(val):
            i = val - row - 1
            temp[col][i] = matrix[row][col]
    copy_matrix(temp, matrix)

def create_matrix(n):
    """creates n by n matrix
    """
    my_list = []
    for i in range(n):
        my_list.append([])
        for j in range(n):
            my_list[i].append(0)
    return my_list

def copy_matrix(current, old):
    """copy matrix to another
    """
    for i in range(len(old)):
        for j in range(len(old[i])):
            old[i][j] = current[i][j]
