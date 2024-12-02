"""
Solves https://adventofcode.com/2024/day/1#part2
"""

from p1_utils import parse_nums

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
    assert similarity_score(*example) == 31
    print(similarity_score(*testdata))
