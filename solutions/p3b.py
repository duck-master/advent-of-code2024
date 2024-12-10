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
    # setup
    instructions = find_instructions(program)
    should_mul = True
    result = 0

    # main loop
    for i, x, y in instructions:
        if i == "don't":
            should_mul = False
        elif i == "do":
            should_mul = True
        elif i == "":
            if should_mul:
                result += int(x) * int(y)
        else:
            raise ValueError(f"Malformed instruction {i}")

    # return
    return result


if __name__ == "__main__":
    assert find_mul_sum(EXAMPLES[3]) == 48
    print(find_mul_sum(TESTS[3]))
