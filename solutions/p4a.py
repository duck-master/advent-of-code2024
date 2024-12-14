"""
Solves https://adventofcode.com/2024/day/4
"""

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

def extend_path(start, direction, length, n):
    """
    extends a path in the corresponding direction
    """
    raise NotImplementedError

def extend_paths(grid, current_paths, next_letters):
    """
    extends all paths in current_paths if they can include the next letter
    """
    raise NotImplementedError

def find_XMAS_count(grid):
    """
    finds the number of all paths that read as XMAS
    """
    raise NotImplementedError

if __name__ == "__main__":
    # debugging logic
    stage1 = find_Xes(EXAMPLES[4])

    # main test
    pprint(find_XMAS_count(EXAMPLES[4]))
