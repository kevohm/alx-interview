#!/usr/bin/python3
"""0-nqueens
"""
from sys import exit, argv


def main():
    """entry point
    """
    args = argv
    if len(args) == 2:
        data = args[1]
        try:
            data = int(data)
        except ValueError:
            print("N must be a number")
            exit(1)

        if data < 4:
            print("N must be at least 4")
            exit(1)
        instance = Queen(data)
        ans = instance.frame_ans()
        for i in ans:
            print(i)
    else:
        print("Usage: nqueens N")
        exit(1)


class Queen():
    """n_queens
    """
    def __init__(self, n):
        """initialize object
        """
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

    def frame_ans(self):
        """convert to required ans
        """
        ans = self.get_ans()
        final = []
        for k, v in enumerate(ans):
            art = []
            for i, j in enumerate(v):
                art.append([i, j])
            final.append(art)
        return final


if __name__ == "__main__":
    main()
