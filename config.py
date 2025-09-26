GRID_ROWS = 8
GRID_COLS = 13
INITIAL_SCORE = 50
INITIAL_ATTEMPTS = 2

CONDITIONAL_TABLES = {
    0: {"red": 1.0, "orange": 0.0, "yellow": 0.0, "green": 0.0},
    1: {"red": 0.2, "orange": 0.6, "yellow": 0.15, "green": 0.05},
    3: {"red": 0.05, "orange": 0.15, "yellow": 0.5, "green": 0.3},
    5: {"red": 0.01, "orange": 0.04, "yellow": 0.15, "green": 0.8},
}

DIRECTION_TABLES = {
    "North": {"North": 0.7, "South": 0.1, "East": 0.1, "West": 0.1, "Here": 0.0},
    "South": {"North": 0.1, "South": 0.7, "East": 0.1, "West": 0.1, "Here": 0.0},
    "East":  {"North": 0.1, "South": 0.1, "East": 0.7, "West": 0.1, "Here": 0.0},
    "West":  {"North": 0.1, "South": 0.1, "East": 0.1, "West": 0.7, "Here": 0.0},
    "Here":  {"North": 0.0, "South": 0.0, "East": 0.0, "West": 0.0, "Here": 1.0},
}