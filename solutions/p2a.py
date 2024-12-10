"""
Solves https://adventofcode.com/2024/day/2
"""

from utils import EXAMPLES, TESTS

def is_report_safe(report):
    """
    Determines whether the given report is safe

    Args:
    * report (list[int]): The report.

    Returns:
    * bool: Whether the report is safe.
    """
    # TODO
    raise NotImplementedError


def count_safe_reports(reports):
    """
    Counts the number of safe reports.

    Args:
    * reports (list[list[int]]): The list of reports.

    Returns:
    * int: The total number of safe reports
    """
    #TODO
    raise NotImplementedError


if __name__ == "__main__":
    assert count_safe_reports(EXAMPLES[1]) == 2
