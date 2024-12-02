"""
Solves https://adventofcode.com/2024/day/1
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

def find_diffs(l1, l2):
    """
    Finds sum of diffs between l1 and l2 after sorting
    """
    sorted_l1 = list(sorted(l1))
    sorted_l2 = list(sorted(l2))
    return sum(abs(a - b) for a, b in zip(sorted_l1, sorted_l2))

if __name__ == "__main__":
    example = parse_nums("../data/example_p1a.txt")
    assert find_diffs(*example) == 11

    test_data = parse_nums("../data/test_p1a.txt")
    print(find_diffs(*test_data))
