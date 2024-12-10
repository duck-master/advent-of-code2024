"""
Solves https://adventofcode.com/2024/day/2#part2

Functions:
* is_report_now_safe(report)
* count_new_safe_reports(reports)
"""

from utils import EXAMPLES
from p2a import is_report_safe

def is_report_now_safe(report):
    """
    Determines whether the report is safe with at most one bad level
    """
    # try the original report
    if is_report_safe(report):
        return True

    # if unsafe, try removing every level one at a time
    for i, _ in enumerate(report):
        new_report = report[:i] + report[i + 1:]
        if is_report_safe(new_report):
            return True

    # if that doesn't work, we know it's false
    return False


def count_new_safe_reports(reports):
    """"
    Counts the number of safe reports
    """
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    # debug logic
    for example_report in EXAMPLES[1]:
        print(is_report_now_safe(example_report))

    assert count_new_safe_reports(EXAMPLES[1]) == 4
