"""
Solves https://adventofcode.com/2024/day/5
"""

from utils import EXAMPLES, TESTS

def check_update_in_order(update, ordering_rules):
    """
    Checks if this particular update is in order
    """
    # main loop
    for rule in ordering_rules:
        first, second = rule
        # skip the rule if irrelevant
        if first not in update or second not in update:
            continue

        # otherwise, find both indices
        first_index = update.index(first)
        second_index = update.index(second)
        if first_index >= second_index:
            return False            # return immediately

    # if all rules work, return True
    return True

def get_middle_number(update):
    """
    Gets the middle number of the update
    """
    len_update = len(update)
    middle = (len_update - 1)//2
    return update[middle]


def get_sum_of_correct_updates(input_data):
    """
    Gets the sum of the correct updates
    """
    ordering_rules, updates = input_data
    result = 0
    for update in updates:
        if check_update_in_order(update, ordering_rules):
            result += get_middle_number(update)
    return result


if __name__ == "__main__":
    assert get_sum_of_correct_updates(EXAMPLES[5]) == 143
    print(get_sum_of_correct_updates(TESTS[5]))
