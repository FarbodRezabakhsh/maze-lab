from dataclasses import dataclass
import numpy as np
from typing import Any, Tuple, List, Optional

# Wall bit‑flags
UP, RIGHT, DOWN, LEFT = 1, 2, 4, 8
ALL_WALLS = UP | RIGHT | DOWN | LEFT  # 0b1111

@dataclass
class MazeCell:
    walls: int = ALL_WALLS

    def has_wall(self, direction: int) -> bool:
        return (self.walls & direction) != 0

    def remove_wall(self, direction: int) -> None:
        self.walls &= ~direction

    def add_wall(self, direction: int) -> None:
        self.walls |= direction

class Maze:
    rows: int
    cols: int
    grid: np.ndarray[Any, np.dtype[object]]  # 2D array of MazeCell

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        # object‑dtype ndarray of MazeCell
        self.grid = np.array(
            [[MazeCell() for _ in range(cols)] for _ in range(rows)],
            dtype=object
        )

    def describe(self) -> None:
        print(f"Maze has {self.rows} rows and {self.cols} columns.")

    def render_ascii(self, path: Optional[List[Tuple[int, int]]] = None) -> None:
        """
        Print an ASCII representation of the maze to the console.
        Optionally overlay a solution path as dots.
        """
        path_set = set(path or [])

        # Top border
        top_border = " _" * self.cols
        print(top_border)

        for r in range(self.rows):
            row_str = "|"
            for c in range(self.cols):
                cell = self.grid[r, c]

                # Mark path with '.' in place of the bottom character
                if (r, c) in path_set:
                    bottom_char = "."
                else:
                    bottom_char = "_" if cell.has_wall(DOWN) else " "

                # Right wall
                right_char = "|" if cell.has_wall(RIGHT) else " "

                row_str += bottom_char + right_char
            print(row_str)