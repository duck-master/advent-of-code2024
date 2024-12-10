"""
Solves https://adventofcode.com/2024/day/3

Functions:
* find_muls(program)
* find_mul_sum(program)
"""

import re
from utils import EXAMPLES, TESTS

MUL_REGEX = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def find_muls(program):
    """
    Finds instances of mul(X, Y) in the program

    Args:
    * program (str): The input program

    Returns:
    * list[tuple[int]]: The found multiplication instructions.
    """
    return re.findall(MUL_REGEX, program)

def find_mul_sum(program):
    """
    Finds the sum of all mul(X, Y) instructions in the program

    Args:
    * program (str): The input program

    Returns:
    * int: The sum of the found multiplication instructions.
    """
    muls_found = find_muls(program)
    result = 0
    for x, y in muls_found:
        result += int(x) * int(y)
    return result

if __name__ == "__main__":
    assert find_mul_sum(EXAMPLES[2]) == 161
    print(find_mul_sum(TESTS[2]))
