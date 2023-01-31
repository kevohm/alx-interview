#!/usr/bin/python3
"""0-nqueens
"""
import sys


class Queen():
    """n_queens
    """
    def __init__(self, n):
        """initialize object
        """
        if not isinstance(n, int):
            print("N must be a number")
            sys.exit(1)
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        self.store = []
        self.n = n
        self.state = []

    def find_all(self):
        """find all possible choices
        """
        if not self.state:
            return range(self.n)

        position = len(self.state)
        possibilities = set(range(self.n))
        for row, col in enumerate(self.state):
            possibilities.discard(col)
            d = position - row
            possibilities.discard(col + d)
            possibilities.discard(col - d)
        return possibilities

    def check_validity(self):
        """check if valid
        """
        return len(self.state) == self.n

    def get_safe_areas(self):
        """get safe areas and print to state
        """
        if self.check_validity():
            self.store.append(self.state.copy())
            return 
        for i in self.find_all():
            self.state.append(i)
            self.get_safe_areas()
            self.state.pop()
    def get_ans(self):
        """return answer
        """
        self.get_safe_areas()
        return self.store

