#!/usr/bin/env python3
"""0-validate_utf8
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    for i in data:
        if len(bin(i)) > 10:
            return False
    return True
