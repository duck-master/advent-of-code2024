"""
Solves https://adventofcode.com/2024/day/1#part2
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

def appearance_count_dict(somelist):
    """
    Dict of {number: times it appears}
    """
    result = {}
    for n in somelist:
        if n in result:
            result[n] += 1
        else:
            result[n] = 1
    return result

if __name__ == "__main__":
    example_l1, example_l2 = parse_nums("../data/example_p1a.txt")
