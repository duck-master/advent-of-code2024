"""
Solves https://adventofcode.com/2024/day/3#part2
"""

import re
from utils import EXAMPLES, TESTS

def find_instructions(program):
    """
    Finds do(), don't(), or mul(X, Y) instructions
    """
    # TODO
    raise NotImplementedError


def find_mul_sum(program):
    """
    Finds the sum of the instructions found
    """
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    assert find_mul_sum(EXAMPLES[2]) == 48
