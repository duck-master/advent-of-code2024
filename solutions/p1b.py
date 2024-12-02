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

def similarity_score(l1, l2):
    """
    Finds the similarity score between l1 and l2
    """
    acd_l2 = appearance_count_dict(l2)
    score = 0
    for n in l1:
        if n in acd_l2:
            score += n * acd_l2[n]
    return score

if __name__ == "__main__":
    example = parse_nums("../data/example_p1a.txt")
    assert similarity_score(*example) == 31
