# GitHub Copilot Instructions

## Project Overview

You are assisting with a Flask-based Sudoku application.

The goal is to improve the existing application while preserving its current functionality and API behavior. All new features should integrate with the current codebase without breaking existing routes or tests.

---

## General Guidelines

- Follow Python PEP 8 coding standards.
- Write clean, readable, and maintainable code.
- Refactor duplicated logic into reusable functions and modules.
- Use meaningful variable and function names.
- Keep HTML, CSS, and JavaScript in separate files.
- Preserve existing functionality while adding new features.
- Handle errors gracefully.
- Add comments only where they improve readability.
- Write code that is compatible with pytest.
- Use Flask best practices.

---

## Project Requirements

### Sudoku Generation

- Generate valid Sudoku puzzles.
- Every generated puzzle must have exactly one valid solution.
- Validate uniqueness before returning a puzzle.
- Keep puzzle generation independent from Flask route handling.

### Difficulty Levels

Support three difficulty levels:

- Easy
- Medium
- Hard

Difficulty should control the number of prefilled cells.

Allow the `/new` route to accept either:

- `difficulty=easy|medium|hard`
- `clues=<number>`

If both are provided, the explicit clue count should take precedence.

---

### Hint Feature

Provide a Hint feature that:

- fills exactly one empty cell
- uses the server-side solution
- locks the hinted cell so users cannot edit it
- does not reveal multiple cells at once

Do not expose the complete solution to the browser.

---

### Check Feature

Keep the existing `/check` route compatible.

The route should:

- compare the submitted board against the stored solution
- return incorrect cell coordinates
- preserve the existing JSON response format

---

### Timer

Implement a client-side timer that:

- starts when a new game begins
- stops when the puzzle is solved
- displays elapsed time in minutes and seconds

The timer should not require backend changes.

---

### Leaderboard

Maintain a Top 10 leaderboard using browser localStorage.

Each leaderboard entry should contain:

- Player name
- Completion time
- Difficulty level
- Number of hints used

Sort entries by completion time and retain only the best ten results.

---

### User Interface

Create a responsive interface that works on desktop and mobile.

Include:

- Dark mode toggle
- Responsive Sudoku grid
- Clearly separated 3×3 boxes using alternating background colors
- Locked cells styled differently from editable cells

---

## Constraints

- Do not break existing Flask routes.
- Keep existing API response formats unchanged.
- Keep the Sudoku solution on the server.
- Lock original puzzle cells and hint-filled cells.
- Preserve compatibility with all existing pytest tests.
- Avoid unnecessary code duplication.
- Prefer small, reusable functions over large functions.

---

## Example Copilot Prompts

### Unique Solution

"Modify the Sudoku generator so every generated puzzle has exactly one valid solution while preserving the existing API."

### Difficulty Levels

"Add Easy, Medium, and Hard difficulty levels that control the number of prefilled cells without breaking the current `/new` route."

### Hint Feature

"Implement a Hint feature that fills exactly one empty cell using the server-side solution and locks the cell afterward."

### Leaderboard

"Create a Top 10 leaderboard using browser localStorage that stores player name, completion time, difficulty, and hints used."

### Grid Styling

"Improve the Sudoku board styling by highlighting each 3×3 section with alternating colors while keeping the layout responsive."

### Dark Mode

"Implement a Dark Mode toggle that updates the entire interface and remembers the user's preference using localStorage."