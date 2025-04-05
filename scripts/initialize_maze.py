import sys
import os

# Force Python to see the project root directory (same trick as before)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from maze_lib.maze_representation import Maze

def main():
    # Create a 5x5 maze
    maze = Maze(5, 5)

    # Print basic info
    maze.describe()

if __name__ == "__main__":
    main()