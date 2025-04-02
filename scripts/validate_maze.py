import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

import random
from maze_lib.maze_representation import Maze
from maze_lib.maze_generation import generate_maze_dfs,check_maze_connectivity


def main():
    random.seed(42)  # For consistency in testing
    maze = Maze(5, 5)

    # Generate with DFS so walls are removed in a random spanning-tree pattern
    generate_maze_dfs(maze, 0, 0)

    # Validate connectivity
    is_connected = check_maze_connectivity(maze, 0, 0)

    if is_connected:
        print("Maze is fully connected. Solvable without needing an explicit path!")
    else:
        print("Maze is NOT fully connected. Some cells are isolated.")

if __name__ == "__main__":
    main()
