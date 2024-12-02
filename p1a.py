"""
Solves https://adventofcode.com/2024/day/1
"""

def parse_nums(textlines):
    """
    Parses a list of textlines
    """
    l1 = []
    l2 = []
    for l in textlines:
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
    print("hello world")
