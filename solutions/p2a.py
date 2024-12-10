"""
Solves https://adventofcode.com/2024/day/2

Functions:
* is_monotonic(report)
* change_within_bounds(report)
* is_report_safe(report)
* count_safe_reports(reports)
"""

from utils import EXAMPLES, TESTS

def is_monotonic(report):
    """
    Determines if the report is monotonic.

    Args:
    * report (list[int]): The report.

    Returns:
    * bool: Whether the report is monotonic
    """
    # edge case
    if report[1] == report[0]:
        return False

    # check whether it should increase
    should_increase = (report[1] > report[0])

    # main loop
    for next_val, prev_val in zip(report[1:], report[:-1]):
        if next_val == prev_val:
            return False
        if (next_val > prev_val) != should_increase:
            return False

    return True

def change_within_bounds(report):
    """
    Determines if the consecutive differences are at most 3 in absolute value.

    Args:
    * report (list[int]): The report

    Returns:
    * bool: Whether the report has this property
    """
    for next_val, prev_val in zip(report[1:], report[:-1]):
        if abs(next_val - prev_val) > 3:
            return False
    return True

def is_report_safe(report):
    """
    Determines whether the given report is safe

    Args:
    * report (list[int]): The report.

    Returns:
    * bool: Whether the report is safe.
    """
    return is_monotonic(report) and change_within_bounds(report)


def count_safe_reports(reports):
    """
    Counts the number of safe reports.

    Args:
    * reports (list[list[int]]): The list of reports.

    Returns:
    * int: The total number of safe reports
    """
    count = 0
    for report in reports:
        if is_report_safe(report):
            count += 1
    return count


if __name__ == "__main__":
    assert count_safe_reports(EXAMPLES[1]) == 2
    print(count_safe_reports(TESTS[1]))
