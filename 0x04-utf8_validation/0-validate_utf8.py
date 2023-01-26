#!/usr/bin/python3
"""0-validate_utf8
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    for i in data:
        d = bin(i)
        key = int(d[0:9], 2)
        if i != key:
            return False
    return True
