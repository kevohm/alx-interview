#!/usr/bin/python3
"""module 0-making_change
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount total
    """
    coins.sort(reverse=True)
    div = 0
    for i in coins:
        quotient = int(total / i)
        rem = total % i
        if (quotient > 0):
            div += quotient
        total = rem
    if total > 0:
        div = -1
    return div
