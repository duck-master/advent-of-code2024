"""
Defines the utility function parse_nums

Functions:
* parse_p1(input_lines)
* parse_p2(input_lines)
* concatenator(input_lines)
* parse_file_group(parsers, file_ids, filepath_template)

Data:
* PARSERS
* NO_PROBLEMS_SOLVED
* PROBLEM_RANGE
* EXAMPLE_FILES
* TEST_FILES
* EXAMPLES
* TESTS
"""

def parse_p1(input_lines):
    """
    Parses problem 1 (each line has two numbers, and the result is two lists).

    Args:
    * input_lines (list[str]): The input lines.

    Returns:
    * tuple[list[int]]: The output data. The tuple has exactly 2 items.
    """
    l1 = []
    l2 = []
    for l in input_lines:
        ls = l.split("   ")
        l1.append(int(ls[0]))
        l2.append(int(ls[1]))
    return l1, l2

def parse_p2(input_lines):
    """
    Parses problem 2 (each line becomes a list of numbers, for a 2D list in total).

    Args:
    * input_lines (list[str]): The input lines.

    Returns:
    * list[list[int]]: The output data.
    """
    result = []
    for l in input_lines:
        num_strings = l.split(" ")
        nums = [int(n) for n in num_strings]
        result.append(nums)
    return result

def concatenator(input_lines):
    """
    Concatenates everything
    """
    return "".join(input_lines)

def parse_file_group(parsers, file_ids, filepath_template):
    """
    Parses a group of files at once.

    Args:
    * parsers (iterable[callable]): A list of functions.
    * file_ids (iterable[str]): A list of file paths.
    * filepath_template (str): A template for the file paths (the id should be named "file_id").
    """
    result = []
    # main loop
    for parser, file_id in zip(parsers, file_ids):
        filepath = filepath_template.format(file_id = file_id)
        with open(filepath, mode = "r", encoding = "utf-8") as f:
            file_content = f.readlines()
        parsed_content = parser(file_content)
        result.append(parsed_content)
    return result


# some auxiliary constants to prepare EXAMPLES and TESTS
# expand as needed
PARSERS = [
    parse_p1,
    parse_p2,
    concatenator,
    concatenator,
    concatenator
]

EXAMPLE_FILE_IDS = ["1", "2", "3a", "3b", "4"]
TEST_FILE_IDS = ["1", "2", "3", "3", "4"]

# get example and test data
EXAMPLES = parse_file_group(
    parsers = PARSERS,
    file_ids = EXAMPLE_FILE_IDS,
    filepath_template = "../data/example_p{file_id}.txt"
    )
TESTS = parse_file_group(
    parsers = PARSERS,
    file_ids = TEST_FILE_IDS,
    filepath_template = "../data/test_p{file_id}.txt"
    )
