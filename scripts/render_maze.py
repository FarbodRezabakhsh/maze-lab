import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

import random
from maze_lib.maze_representation import Maze
from maze_lib.maze_generation import generate_maze_dfs

def main():
    random.seed(42)  # Keep consistent for testing
    maze = Maze(5, 5)
    generate_maze_dfs(maze, 0, 0)

    print("ASCII representation of the generated maze:\n")
    maze.render_ascii()

if __name__ == "__main__":
    main()
