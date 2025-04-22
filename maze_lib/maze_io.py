
import json
from maze_lib.maze_representation import Maze, MazeCell

def save_maze(maze: Maze, filename: str) -> None:
    """
    Save the Maze object to a JSON file.
    We store rows, cols, and the grid as a nested list of wall‐bit integers.
    """
    data = {
        "rows": maze.rows,
        "cols": maze.cols,
        "grid": [
            [cell.walls for cell in row]   # grab the bitmask int
            for row in maze.grid
        ]
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
    grid_data = data["grid"]  # nested lists of ints

    maze = Maze(rows, cols)
    # overwrite each cell with the saved wall‐bit
    for r, row in enumerate(grid_data):
        for c, walls in enumerate(row):
            maze.grid[r, c] = MazeCell(walls)

    return maze
