#!/usr/bin/python3
"""calculates the fewest number of operations needed to result
in exactly n H characters in the file"""


def minOperations(n):
    data = "H"
    copy = ""
    for i in range(1, n+1):
        if len(data) == n:
            return i
        if len(copy) + len(data) == n:
            return i
        elif i % 3 == 1:
            copy = data
        else:
            if len(copy) != 0:
                data = copy + data
    print(data)
