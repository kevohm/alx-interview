#!/usr/bin/python3
"""test_queen
"""
Queen = __import__("0-nqueens").Queen


obj = Queen(4)
print(obj.state, obj.n)
