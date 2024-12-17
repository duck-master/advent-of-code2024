"""
Solves https://adventofcode.com/2024/day/4
"""

from pprint import pprint
from utils import EXAMPLES

#hardcode all the valid directions
DIRECTIONS = {
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
}

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

def extend_path(start, direction, length):
    """
    extends a path in the corresponding direction
    """
    x_s, y_s = start
    x_d, y_d = direction
    result = [(x_s + i*x_d, y_s + i*y_d)
              for i in range(length)
              ]
    return result

def read_path(grid, path):
    """
    Reads the sequence of symbols in the path
    """
    n = len(grid)
    result = []
    for x, y in path:
        # ignore paths that go outside bounds
        if x not in range(n) or y not in range(n):
            return None

        result.append(grid[x][y])
    return "".join(result)

def find_XMASes(grid):
    """
    finds all paths that read as XMAS
    returns a list
    """
    result = []
    all_Xes = find_Xes(grid)
    for start in all_Xes:
        for direction in DIRECTIONS:
            possible_path = extend_path(start, direction, 4)
            if read_path(grid, possible_path) == "XMAS":
                result.append(possible_path)
    return result

def find_XMAS_count(grid):
    """
    finds the number of all paths that read as XMAS
    """
    return len(

if __name__ == "__main__":
    # debugging logic
    stage1 = find_Xes(EXAMPLES[4])
    pprint(stage1)

    # main test
    pprint(find_XMAS_count(EXAMPLES[4]))
