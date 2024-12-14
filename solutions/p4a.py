"""
Solves https://adventofcode.com/2024/day/4
"""

from itertools import product
from utils import EXAMPLES

def find_Xes(grid):
    """
    finds all X's
    """
    result = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "X":
                result.append((x, y))
    return result

def next_range(x, n):
    """
    range(x - 1, x + 1) intersect range(0, n) as a list
    """
    if x < 0:
        return None
    elif x == 0:
        return [0, 1]
    elif x < n - 1:
        return [x - 1, x, x + 1]
    elif x == n - 1:
        return [n - 2, n - 1]
    else:
        return None

def find_neighbors(coords, n):
    """
    Finds neighbors of the given coords (in N by N board)
    """
    x, y = coords
    return list(product(
        next_range(x, n),
        next_range(y, n)
        ))


def extend_path(grid, current_paths, next_letter):
    """
    extends all paths in current_paths if they can include the next letter
    """
    # TODO
    raise NotImplementedError

def find_XMAS_count(grid):
    """
    finds the number of all paths that read as XMAS
    """
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    # debugging logic
    print(find_Xes(EXAMPLES[4]))
    # main test
    print(find_XMAS_count(EXAMPLES[4]))
