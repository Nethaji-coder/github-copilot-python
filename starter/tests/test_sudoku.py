import sudoku_logic
from app import CURRENT


def assert_complete_solution(board):
    assert len(board) == sudoku_logic.SIZE
    for row in board:
        assert len(row) == sudoku_logic.SIZE

    for row in board:
        assert set(row) == set(range(1, sudoku_logic.SIZE + 1))

    for col in range(sudoku_logic.SIZE):
        values = [board[row][col] for row in range(sudoku_logic.SIZE)]
        assert set(values) == set(range(1, sudoku_logic.SIZE + 1))

    for box_row in range(0, sudoku_logic.SIZE, 3):
        for box_col in range(0, sudoku_logic.SIZE, 3):
            values = []
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    values.append(board[row][col])
            assert set(values) == set(range(1, sudoku_logic.SIZE + 1))


def test_generate_puzzle_returns_puzzle_and_solution():
    puzzle, solution = sudoku_logic.generate_puzzle(35)

    assert isinstance(puzzle, list)
    assert isinstance(solution, list)
    assert len(puzzle) == sudoku_logic.SIZE
    assert len(solution) == sudoku_logic.SIZE
    assert puzzle != solution
    assert_complete_solution(solution)
    assert sum(cell == sudoku_logic.EMPTY for row in puzzle for cell in row) > 0


def test_index_route_renders_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_new_game_route_populates_current_state(client):
    response = client.get("/new?clues=30")
    assert response.status_code == 200

    payload = response.get_json()
    assert isinstance(payload["puzzle"], list)
    assert len(payload["puzzle"]) == sudoku_logic.SIZE
    assert CURRENT["puzzle"] is not None
    assert CURRENT["solution"] is not None


def test_check_solution_route_reports_incorrect_cells(client):
    _, solution = sudoku_logic.generate_puzzle(35)
    CURRENT["solution"] = solution

    board = [row[:] for row in solution]
    board[0][0] = 2 if board[0][0] != 1 else 1

    response = client.post("/check", json={"board": board})
    assert response.status_code == 200

    payload = response.get_json()
    assert payload["incorrect"] == [[0, 0]]
