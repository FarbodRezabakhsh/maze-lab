"""
Implements a DFS-based approach to "carve" passages in a Maze,
ensuring there's exactly one connected component (i.e., solvable by design).
"""

import random
from maze_lib.maze_representation import Maze


def generate_maze_dfs(maze: Maze, start_row=0, start_col=0):
    """
    Modify the given maze in place using Depth-First Search backtracking.
    We'll knock down walls to create a solvable maze.

    :param maze: Maze instance (rows x cols) with all walls initially True
    :param start_row: row index to begin DFS
    :param start_col: column index to begin DFS
    """
    rows, cols = maze.rows, maze.cols

    # A 2D array to track if a cell is visited during generation
    visited = [[False] * cols for _ in range(rows)]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Directions: (row_change, col_change, wall_to_remove, opposite_wall)
    directions = [
        (-1, 0, "up", "down"),  # up
        (0, 1, "right", "left"),  # right
        (1, 0, "down", "up"),  # down
        (0, -1, "left", "right"),  # left
    ]

    def dfs(r, c):
        visited[r][c] = True
        # Shuffle directions so the maze paths are random
        random.shuffle(directions)

        for dr, dc, wall_current, wall_next in directions:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and not visited[nr][nc]:
                # Knock down the wall between current cell and next cell
                maze.grid[r][c][wall_current] = False
                maze.grid[nr][nc][wall_next] = False

                # Recursively visit the neighbor
                dfs(nr, nc)

    # Start the DFS from the specified cell
    dfs(start_row, start_col)

