
"""
Provides functions to serialize (save) and deserialize (load) a Maze.
"""
import json
from maze_lib.maze_representation import Maze


def save_maze(maze: Maze, filename: str):
    """
    Save the Maze object to a JSON file.
    We store rows, cols, and the grid (the wall info for each cell).
    """
    data = {
        "rows": maze.rows,
        "cols": maze.cols,
        "grid": maze.grid  # grid is a 2D list of dicts with up/right/down/left
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_maze(filename: str) -> Maze:
    """
    Load Maze data from a JSON file and return a Maze object with the same walls.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    rows = data["rows"]
    cols = data["cols"]
    grid_data = data["grid"]  # 2D list of dicts

    # Create a Maze object with the same dimensions
    maze = Maze(rows, cols)
    # Overwrite the default grid (all True) with what we loaded
    maze.grid = grid_data
    return maze
