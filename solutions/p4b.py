"""
Solves https://adventofcode.com/2024/day/4#part2
"""

from utils import EXAMPLES
from p4a import find_chars

def read_cross(grid, center):
    """
    Reads the points at a cross
    """
    #TODO
    raise NotImplementedError


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
