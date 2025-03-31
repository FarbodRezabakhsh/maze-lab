

"""
Contains the Maze class to represent a grid-based maze.
Each cell tracks whether its four walls (up/down/left/right) are present.
"""

class Maze:
    def __init__(self, rows, cols):
        """
            Initialize the maze with a given number of rows and columns.
            By default, every cell starts fully enclosed by walls.
        """
        self.rows = rows
        self.cols = cols

        self.grid = []
        for r in range(rows):
            row_data = []
            for c in range(cols):
                # each cell has walls: up, right, down, left
                cell_walls = {
                    "up":True,
                    "down":True,
                    "left":True,
                    "right":True,
                }
                row_data.append(cell_walls)
            self.grid.append(row_data)

    def describe(self):
        """
        Print a brief description of the maze dimensions and wall status.
        """
        print(f"Maze has {self.rows} rows and {self.cols} columns.")


