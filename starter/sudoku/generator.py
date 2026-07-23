import random

from .board_utils import create_empty_board, deep_copy
from .constants import EMPTY, SIZE
from .solver import fill_board, has_unique_solution


def remove_cells(board, clues):
    attempts = SIZE * SIZE - clues
    cells = [(row, col) for row in range(SIZE) for col in range(SIZE)]
    random.shuffle(cells)

    removed = 0
    while removed < attempts and cells:
        row, col = cells.pop()
        if board[row][col] == EMPTY:
            continue

        original_value = board[row][col]
        board[row][col] = EMPTY
        if not has_unique_solution(board):
            board[row][col] = original_value
            continue

        removed += 1


def generate_puzzle(clues=35, difficulty=None):
    board = create_empty_board()
    fill_board(board)
    solution = deep_copy(board)
    puzzle = deep_copy(board)
    clue_count = clues if clues is not None else 35
    remove_cells(puzzle, clue_count)
    return puzzle, solution
