"""
Solves https://adventofcode.com/2024/day/5#part2
"""

from utils import EXAMPLES
from p5a import check_update_in_order, get_middle_number

def find_topological_order(ordering_rules):
    """
    Finds the topological order
    """
    raise NotImplementedError


def reorder_update(update, topological_order):
    """
    Reorders the update to conform with the topological order
    """
    raise NotImplementedError


def find_sum_of_reordered_middles(input_data):
    """
    Finds the sum of the reordered middles of updates
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(find_sum_of_reordered_middles(EXAMPLES[5]))