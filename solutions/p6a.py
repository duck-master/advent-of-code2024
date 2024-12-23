"""
Solves https://adventofcode.com/2024/day/6
"""

from utils import EXAMPLES

def move_guard_one_step(board, guard_position, direction):
    """
    Moves the guard exactly one step
    Returns (new guard position, new direction)
    """
    # TODO
    raise NotImplementedError


def simulate_guard(board, guard_position, direction):
    """
    Simulate the guard until it leaves the mapped area
    Returns the list of positions visited in order
    """
    #TODO
    raise NotImplementedError


def find_position_count_visited(board, guard_position, direction):
    """
    Finds the number of positions visited
    """
    #TODO
    raise NotImplementedError

if __name__ == "__main__":
    print(find_position_count_visited(EXAMPLES[5]))
