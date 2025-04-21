

"""
Contains the Maze class to represent a grid-based maze.
Each cell tracks whether its four walls (up/down/left/right) are present.
"""
from dataclasses import dataclass
import numpy as np

UP, RIGHT, DOWN, LEFT = 1, 2, 4, 8
ALL_WALLS = UP | DOWN | LEFT | RIGHT # All walls present (0b1111)

@dataclass
class MazeCell:
    walls: int = ALL_WALLS

    def has_wall(self, direction: int) -> bool:
        return (self.walls & direction) != 0

    def remove_wall(self, direction: int) -> None:
        self.walls &= ~direction

    def add_walls(self, direction: int) -> None:
        self.walls |= direction


class Maze:
    def __init__(self, rows, cols):
        """
            Initialize the maze with a given number of rows and columns.
            By default, every cell starts fully enclosed by walls.
        """
        self.rows = rows
        self.cols = cols
        # store maze as NumPy ndarray of MazeCell objects
        self.grid = np.array([[MazeCell() for _ in range(cols)] for _ in range(rows)], dtype=object)

    def describe(self):
        """
        Print a brief description of the maze dimensions and wall status.
        """
        print(f"Maze has {self.rows} rows and {self.cols} columns.")

    def render_ascii(self):
        top_border = " _" * self.cols
        print(top_border)

        for r in range(self.rows):
            row_str = "|"
            for c in range(self.cols):
                cell = self.grid[r, c]
                bottom_char = "_" if cell.has_wall(DOWN) else " "
                right_char = "|" if cell.has_wall(RIGHT) else " "
                row_str += bottom_char + right_char
            print(row_str)