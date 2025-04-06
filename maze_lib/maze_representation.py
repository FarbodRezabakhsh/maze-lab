

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
                    "up":True, # means "closed"
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

    def render_ascii(self):
        """
        Print an ASCII representation of the maze to the console.
        Each cell is represented by spaces and walls.
        """
        rows = self.rows
        cols = self.cols

        # Top border
        top_border = " _" * cols
        print(top_border)

        for r in range(rows):
            # Start each row with a vertical border
            row_str = "|"
            for c in range(cols):
                cell_walls = self.grid[r][c]

                # If "down" is True => there's a wall at the bottom
                # We show "_" or " " accordingly
                if cell_walls["down"]:
                    bottom_char = "_"
                else:
                    bottom_char = " "

                # If "right" is True => there's a right wall
                # We show "|" else just " "
                if cell_walls["right"]:
                    right_char = "|"
                else:
                    right_char = " "

                # Put them together
                row_str += bottom_char + right_char
            print(row_str)