#!/usr/bin/python3
"""0-nqueens
"""
import sys


class Queen():
    """n_queens
    """
    __state = []
    def __init__(self, n):
        """initialize object
        """
        if not isinstance(n, int):
            print("N must be a number")
            sys.exit(1)
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        __state = []
        self.n = n
        self.state = []

    def find_all(self):
        """find all possible choices
        """
    def check_validity(self):
        """check if valid
        """
    def get_safe_areas(self):
        """get safe areas and print to state
        """
