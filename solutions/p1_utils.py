"""
Defines the utility function parse_nums
"""

def parse_nums(input_file):
    """
    Parses a list of textlines from the input file
    """
    l1 = []
    l2 = []
    with open(input_file, mode = "r", encoding = "utf-8") as f:
        for l in f:
            ls = l.split("   ")
            l1.append(int(ls[0]))
            l2.append(int(ls[1]))
    return l1, l2

example = parse_nums("../data/example_p1.txt")
test_data = parse_nums("../data/test_p1.txt")
