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

if __name__ == "__main__":
    print("hello world")
