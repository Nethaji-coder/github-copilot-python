DEFAULT_DIFFICULTY = "medium"

DIFFICULTY_CLUES = {
    "easy": 40,
    "medium": 32,
    "hard": 24,
}


def normalize_difficulty(difficulty=None, clues=None):
    if difficulty is None:
        difficulty = DEFAULT_DIFFICULTY
    if isinstance(difficulty, str):
        lowered = difficulty.strip().lower()
        if lowered in DIFFICULTY_CLUES:
            return lowered

    if clues is not None:
        return None

    return DEFAULT_DIFFICULTY


def get_clue_count(difficulty=None, clues=None):
    if clues is not None:
        try:
            return int(clues)
        except (TypeError, ValueError):
            return DIFFICULTY_CLUES[DEFAULT_DIFFICULTY]

    normalized = normalize_difficulty(difficulty)
    return DIFFICULTY_CLUES[normalized]
