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
                result.append((x, y))
    return result

def find_neighbors(coords, n):
    """
    Finds neighbors of the given coords (in N by N board)
    """
    # TODO
    raise NotImplementedError

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
