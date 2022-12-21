#!/usr/bin/python3
"""Calculate the pascals's triangle"""


def factorial(n):
    """find factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def combination(n, r):
    """calculating nCr"""
    top = factorial(n)
    bottom = factorial(r)
    bottom = bottom * factorial(n - r)
    return int(top / bottom)


def getPascalRow(n):
    """Pascals values for n"""
    arr = []
    for i in range(0, n + 1):
        arr.append(combination(n, i))
    return arr


def pascal_triangle(n):
    """returns a list of lists of integers"""
    arr = []
    if n < 1:
        return []
    for i in range(0, n):
        arr.append(getPascalRow(i))
    return arr
