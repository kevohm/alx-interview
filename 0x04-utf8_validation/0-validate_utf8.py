#!/usr/bin/python3
"""0-validate_utf8
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    if not isinstance(data, list) or data is None:
        return False
    for i in data:
        try:
            i.to_bytes(2, "big").decode("utf-8")
        except(UnicodeDecodeError):
            return False
    return True
