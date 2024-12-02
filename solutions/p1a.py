"""
Solves https://adventofcode.com/2024/day/1
"""

from p1_utils import parse_nums, example, test_data

def find_diffs(l1, l2):
    """
    Finds sum of diffs between l1 and l2 after sorting
    """
    sorted_l1 = list(sorted(l1))
    sorted_l2 = list(sorted(l2))
    return sum(abs(a - b) for a, b in zip(sorted_l1, sorted_l2))

if __name__ == "__main__":
    assert find_diffs(*example) == 11
    print(find_diffs(*test_data))
