"""
Defines the utility function parse_nums

Functions:
* parse_p1(input_lines)
* parse_file_group(parsers, file_paths)

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
    Parses a list of lines
    """
    l1 = []
    l2 = []
    for l in input_lines:
        ls = l.split("   ")
        l1.append(int(ls[0]))
        l2.append(int(ls[1]))
    return l1, l2

def parse_file_group(parsers, file_paths):
    """
    Parses a group of files at once.

    Args:
    * parsers (iterable[callable]): A list of functions.
    * file_paths (iterable[str]): A list of file paths. 
    """
    result = []
    # main loop
    for parser, filepath in zip(parsers, file_paths):
        with open(filepath, mode = "r", encoding = "utf-8") as f:
            file_content = f.readlines()
        parsed_content = parser(file_content)
        result.append(parsed_content)
    return result


# some auxiliary constants to prepare EXAMPLES and TESTS
# expand as needed
PARSERS = [
    parse_p1
]
NO_PROBLEMS_SOLVED = 1  # increment as needed
PROBLEM_RANGE = range(1, NO_PROBLEMS_SOLVED + 1)    # if separate data for A and B, change this
EXAMPLE_FILES = [f"../data/example_p{n}.txt" for n in PROBLEM_RANGE]
TEST_FILES = [f"../data/test_p{n}.txt" for n in PROBLEM_RANGE]

# get example and test data
EXAMPLES = parse_file_group(PARSERS, EXAMPLE_FILES)
TESTS = parse_file_group(PARSERS, TEST_FILES)