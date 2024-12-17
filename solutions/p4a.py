"""
Solves https://adventofcode.com/2024/day/4
"""

from pprint import pprint
from utils import EXAMPLES

def find_Xes(grid):
    """
    finds all X's
    """
    result = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "X":
                result.append([(x, y)])
    return result

def extend_path(start, direction, length):
    """
    extends a path in the corresponding direction
    """
    #TODO
    raise NotImplementedError

def read_path(grid, path):
    """
    Reads the sequence of symbols in the path
    """
    #TODO
    raise NotImplementedError

def find_XMAS_count(grid):
    """
    finds the number of all paths that read as XMAS
    """
    #TODO
    raise NotImplementedError

if __name__ == "__main__":
    # debugging logic
    stage1 = find_Xes(EXAMPLES[4])

    # main test
    pprint(find_XMAS_count(EXAMPLES[4]))
