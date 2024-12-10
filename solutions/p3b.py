"""
Solves https://adventofcode.com/2024/day/3#part2
"""

import re
from utils import EXAMPLES, TESTS

INSTRUCTION_REGEX = re.compile(r"(do(?:n't)?)\(\)|mul\((\d{1,3}),(\d{1,3})\)")

def find_instructions(program):
    """
    Finds do(), don't(), or mul(X, Y) instructions
    """
    return re.findall(INSTRUCTION_REGEX, program)


def find_mul_sum(program):
    """
    Finds the sum of the instructions found
    """
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    print(find_instructions(EXAMPLES[2]))
    assert find_mul_sum(EXAMPLES[2]) == 48
