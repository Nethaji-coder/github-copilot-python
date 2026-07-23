from flask import Flask, render_template, jsonify, request
import sudoku_logic

app = Flask(__name__)

# Keep a simple in-memory store for current puzzle and solution
CURRENT = {
    'puzzle': None,
    'solution': None,
    'hints_used': 0,
    'locked_cells': []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new_game():
    clues = request.args.get('clues', None)
    difficulty = request.args.get('difficulty', None)
    clue_count = sudoku_logic.get_clue_count(clues=clues, difficulty=difficulty)
    puzzle, solution = sudoku_logic.generate_puzzle(clue_count, difficulty=difficulty)
    CURRENT['puzzle'] = puzzle
    CURRENT['solution'] = solution
    CURRENT['hints_used'] = 0
    CURRENT['locked_cells'] = []
    return jsonify({'puzzle': puzzle})

@app.route('/hint')
def give_hint():
    puzzle = CURRENT.get('puzzle')
    solution = CURRENT.get('solution')
    if puzzle is None or solution is None:
        return jsonify({'error': 'No game in progress'}), 400

    locked_cells = CURRENT.get('locked_cells', [])
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if [i, j] in locked_cells:
                continue
            if puzzle[i][j] == sudoku_logic.EMPTY:
                puzzle[i][j] = solution[i][j]
                CURRENT['hints_used'] += 1
                locked_cells.append([i, j])
                CURRENT['locked_cells'] = locked_cells
                return jsonify({'row': i, 'col': j, 'value': solution[i][j]})

    return jsonify({'error': 'No available hints'}), 400

@app.route('/check', methods=['POST'])
def check_solution():
    data = request.json
    board = data.get('board')
    solution = CURRENT.get('solution')
    if solution is None:
        return jsonify({'error': 'No game in progress'}), 400
    incorrect = []
    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):
            if board[i][j] != solution[i][j]:
                incorrect.append([i, j])
    return jsonify({'incorrect': incorrect})

if __name__ == '__main__':
    app.run(debug=True)