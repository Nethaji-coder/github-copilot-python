import random
from .board_utils import deep_copy
from .constants import EMPTY, SIZE


def is_safe(board, row, col, num):
    for x in range(SIZE):
        if x != col and board[row][x] == num:
            return False
        if x != row and board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            current_row = start_row + i
            current_col = start_col + j
            if (current_row != row or current_col != col) and board[current_row][current_col] == num:
                return False
    return True


def fill_board(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == EMPTY:
                possible = list(range(1, SIZE + 1))
                random.shuffle(possible)
                for candidate in possible:
                    if is_safe(board, row, col, candidate):
                        board[row][col] = candidate
                        if fill_board(board):
                            return True
                        board[row][col] = EMPTY
                return False
    return True


def _is_valid_partial_board(board):
    for row in range(SIZE):
        for col in range(SIZE):
            value = board[row][col]
            if value == EMPTY:
                continue
            if not is_safe(board, row, col, value):
                return False
    return True


def _find_next_empty(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == EMPTY:
                return row, col
    return None, None


def count_solutions(board, limit=2):
    if not _is_valid_partial_board(board):
        return 0

    current_board = deep_copy(board)

    def search(working_board):
        solutions_found = 0
        row, col = _find_next_empty(working_board)
        if row is None:
            return 1

        for candidate in range(1, SIZE + 1):
            if not is_safe(working_board, row, col, candidate):
                continue
            working_board[row][col] = candidate
            solutions_found += search(working_board)
            working_board[row][col] = EMPTY
            if solutions_found >= limit:
                return solutions_found
        return solutions_found

    return search(current_board)


def has_unique_solution(board):
    return count_solutions(board, limit=2) == 1
