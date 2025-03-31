import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

import random
from maze_lib.maze_representation import Maze
from maze_lib.maze_generation import generate_maze_dfs

def main():
    random.seed(42)  # for reproducibility (or remove this line for randomness)
    maze = Maze(5, 5)
    generate_maze_dfs(maze, start_row=0, start_col=0)

    print("Maze (5x5) generated with DFS approach. Some walls are removed.")
    # Optional: Print partial wall info for the top-left cell to see changes
    print("Cell (0,0) walls:", maze.grid[0][0])

    # You could also build a textual "preview" or call a method to see more details.

if __name__ == "__main__":
    main()


