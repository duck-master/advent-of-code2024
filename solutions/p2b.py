"""
Solves https://adventofcode.com/2024/day/2#part2

Functions:
* is_report_now_safe(report)
* count_new_safe_reports(reports)
"""

from utils import EXAMPLES

def is_report_now_safe(report):
    """
    Determines whether the report is safe with at most one bad level
    """
    # TODO
    raise NotImplementedError

def count_new_safe_reports(reports):
    """"
    Counts the number of safe reports
    """
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    assert count_new_safe_reports(EXAMPLES[1]) == 4
