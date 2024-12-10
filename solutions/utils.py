"""
Defines the utility function parse_nums

Functions:
* parse_p1(input_lines)
* parse_file_group(parsers, file_paths)

Data:
* PARSERS
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
    * parsers (list[callable]): A list of functions.
    * file_paths (list[str]): A list of file paths. 
    """
    result = []
    # main loop
    for parser, filepath in zip(parsers, file_paths):
        with open(filepath, mode = "r", encoding = "utf-8") as f:
            file_content = f.readlines()
        parsed_content = parser(file_content)
        result.append(parsed_content)
    return result



# expand as needed
PARSERS = [
    parse_p1
]

#TODO: refactor
#example = parse_nums("../data/example_p1.txt")
#test_data = parse_nums("../data/test_p1.txt")
