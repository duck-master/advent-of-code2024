"""
Solves https://adventofcode.com/2024/day/6
"""

from utils import EXAMPLES

RIGHT_TURN = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

def visualize_board(board, guard_position):
    """
    Visualizes the current board state. For debugging purposes
    """
    result = ""
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if (x, y) == guard_position:
                result += "G"
            elif cell:
                result += "#"
            else:
                result += "."
        result += "\n"
    return result

def add_2D_vecs(vec1, vec2):
    """
    Adds two 2D vectors
    Helper function for move_guard_one_step
    """
    x1, y1 = vec1
    x2, y2 = vec2
    return (x1 + x2, y1 + y2)

def move_guard_one_step(board, guard_position, direction):
    """
    Moves the guard exactly one step
    Returns (new guard position, new direction)
    """
    n = len(board)
    new_position = add_2D_vecs(guard_position, direction)
    npx, npy = new_position

    # if new position out of bounds, then return None
    if out_of_bounds(n, new_position):
        return None

    # if position occupied, turn instead
    if board[npx][npy]:
        new_direction = RIGHT_TURN[direction]
        return (guard_position, new_direction)

    # otherwise, go in that direction
    else:
        return (new_position, direction)

def out_of_bounds(n, position):
    """
    Determines if the position is out of bounds
    """
    x, y = position
    return (x not in range(n)) or (y not in range(n))

def simulate_guard(board, guard_position, direction):
    """
    Simulate the guard until it leaves the mapped area
    Returns the list of positions visited in order
    """
    # simulation variables
    result = []
    current_position = guard_position
    current_direction = direction

    # main loop
    while True:
        next_state = move_guard_one_step(
            board,
            current_position,
            current_direction
            )

        if next_state is None:
            break

        current_position, current_direction = next_state
        result.append(current_position)

    # return
    return result


def find_position_count_visited(board, guard_position, direction):
    """
    Finds the number of positions visited
    """
    positions_visited = simulate_guard(board, guard_position, direction)
    return len(set(positions_visited))

if __name__ == "__main__":
    assert find_position_count_visited(*EXAMPLES[6]) == 41
    print(find_position_count_visited(*TESTS[6]))
