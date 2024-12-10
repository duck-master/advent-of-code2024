"""
Solves https://adventofcode.com/2024/day/2#part2

Functions:
* is_report_now_safe(report)
* count_new_safe_reports(reports)
"""

from utils import EXAMPLES, TESTS
from p2a import is_report_safe

def is_report_now_safe(report):
    """
    Determines whether the report is safe with at most one bad level

    Args:
    * report (list[int]): The report

    Returns:
    * bool: Whether the report has this property
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

    Args:
    * reports (list[list[int]]): The list of reports.

    Returns:
    * int: The total number of safe reports
    """
    count = 0
    for report in reports:
        if is_report_now_safe(report):
            count += 1
    return count

if __name__ == "__main__":
    assert count_new_safe_reports(EXAMPLES[1]) == 4
    print(count_new_safe_reports(TESTS[1]))
