"""
Solves https://adventofcode.com/2024/day/4#part2
"""

from utils import EXAMPLES
from p4a import find_chars

CROSS_DIRECTIONS = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
    ]

def read_cross(grid, center):
    """
    Reads the grid cells in a cross centered at the given center
    """
    n = len(grid)
    x_c, y_c = center

    # return None if out of bounds
    if x_c not in range(1, n - 1) or y_c not in range(n - 1):
        return None

    # main logic
    result = []
    for x_d, y_d in CROSS_DIRECTIONS:
        result.append(grid[x_c + x_d][y_c + y_d])
    return result

def find_X_MASes(grid):
    """
    finds all instances of two MASes in a cross
    returns a list
    """
    #TODO
    raise NotImplementedError


def find_X_MAS_count(grid):
    """
    finds the total number of two MASes in a cross
    """
    #TODO
    raise NotImplementedError

if __name__ == "__main__":
    print(find_X_MAS_count(EXAMPLES[4]))
