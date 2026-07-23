# Flask Sudoku Application

A Sudoku game built using Python Flask. This project refactors legacy Sudoku code and adds new features such as difficulty levels, hints, timer, leaderboard, dark mode, and responsive design.

## Features

### Sudoku Gameplay
- Generates playable Sudoku puzzles
- Easy, Medium, and Hard difficulty levels
- Each puzzle has exactly one valid solution
- Prefilled cells are locked
- Checks incorrect entries in real time
- Displays completion message when solved

### Game Features
- Hint button to fill one correct cell
- Timer to track completion time
- Top 10 leaderboard using browser local storage
- Stores:
  - Player name
  - Completion time
  - Difficulty level
  - Number of hints used

### User Interface
- Responsive design for desktop and mobile
- Dark mode toggle
- Alternating colors for 3x3 Sudoku boxes
- Readable layout in light and dark themes

## Project Structure

```
starter/
│
├── app.py
├── sudoku/
│   ├── solver.py
│   ├── generator.py
│   ├── constants.py
│   ├── difficulty.py
│   └── board_utils.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── main.js
│   └── styles.css
│
├── tests/
│   └── test_sudoku.py
│
└── screenshots/
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000
```

## Running Tests

The project uses pytest for testing.

Run:

```bash
python -m pytest
```

The tests verify:

- Sudoku puzzle generation
- Unique solution validation
- Flask routes
- Hint functionality
- Check solution functionality
- Difficulty handling

## GitHub Copilot Usage

GitHub Copilot was used as an assistant for:

- Setting up pytest testing framework
- Refactoring Sudoku logic into modules
- Adding unique solution validation
- Implementing difficulty levels
- Adding hint and check features
- Creating timer and leaderboard
- Improving UI styling and dark mode

Screenshots of Copilot interactions are available in the `screenshots` folder.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- pytest
- GitHub Copilot