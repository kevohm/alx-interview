#!/usr/bin/python
"""the perimeter of the island described in grid
"""


def island_perimeter(grid):
    p = 0
    height = len(grid)
    for y in range(height):
        width = len(grid[y])
        for x in range(width):
            if(grid[y][x] == 1):
                if y-1 >= 0:
                    if(grid[y-1][x] == 0):
                        p += 1
                if y+1 < height:
                    if(grid[y+1][x] == 0):
                        p += 1
                if x-1 >= 0:
                    if(grid[y][x-1] == 0):
                        p += 1
                if x+1 < width:
                    if(grid[y][x+1] == 0):
                        p += 1
    return p
