"""
Solves https://adventofcode.com/2024/day/3

Functions:
* find_muls(program)
* find_mul_sum(program)
"""

import re
from utils import EXAMPLES, TESTS

def find_muls(program):
    """
    Finds instances of mul(X, Y) in the program
    """
    # TODO
    raise NotImplementedError


def find_mul_sum(program):
    """
    Finds the sum of all mul(X, Y) instructions in the program
    """
    #TODO
    raise NotImplementedError

if __name__ == "__main__":
    assert find_mul_sum(EXAMPLES[2]) == 161
