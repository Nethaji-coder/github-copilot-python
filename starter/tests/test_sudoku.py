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
    assert sudoku_logic.has_unique_solution(puzzle) is True


def test_count_solutions_for_single_empty_cell_is_one():
    _, solution = sudoku_logic.generate_puzzle(35)
    board = [row[:] for row in solution]
    board[0][0] = sudoku_logic.EMPTY

    assert sudoku_logic.count_solutions(board) == 1


def test_has_unique_solution_for_single_empty_cell():
    _, solution = sudoku_logic.generate_puzzle(35)
    board = [row[:] for row in solution]
    board[0][0] = sudoku_logic.EMPTY

    assert sudoku_logic.has_unique_solution(board) is True


def test_difficulty_normalization_is_case_insensitive():
    assert sudoku_logic.normalize_difficulty("easy") == "easy"
    assert sudoku_logic.normalize_difficulty("Easy") == "easy"
    assert sudoku_logic.normalize_difficulty("EASY") == "easy"


def test_default_difficulty_is_used_when_none_is_provided():
    assert sudoku_logic.get_clue_count() == sudoku_logic.DIFFICULTY_CLUES[sudoku_logic.DEFAULT_DIFFICULTY]


def test_clues_parameter_still_overrides_difficulty():
    assert sudoku_logic.get_clue_count(difficulty="hard", clues=50) == 50


def test_hint_route_fills_one_empty_cell_and_locks_it(client):
    response = client.get("/new?clues=35")
    assert response.status_code == 200

    hint_response = client.get("/hint")
    assert hint_response.status_code == 200

    payload = hint_response.get_json()
    assert "row" in payload
    assert "col" in payload
    assert "value" in payload
    assert CURRENT["hints_used"] == 1
    assert [payload["row"], payload["col"]] in CURRENT["locked_cells"]


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
    board[0][0] = 1 if board[0][0] != 1 else 2

    response = client.post("/check", json={"board": board})
    assert response.status_code == 200

    payload = response.get_json()
    assert payload["incorrect"] == [[0, 0]]
