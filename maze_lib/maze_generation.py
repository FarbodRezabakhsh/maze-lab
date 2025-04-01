"""
Implements a DFS-based approach to "carve" passages in a Maze,
ensuring there's exactly one connected component (i.e., solvable by design).
"""

import random
from maze_lib.maze_representation import Maze
from collections import deque

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

def check_maze_connectivity(maze: Maze, start_row=0, start_col=0):
    """
    Perform a BFS/DFS to ensure that from (start_row, start_col),
    we can reach all other cells in the maze (i.e. it's fully connected).

    :param maze: an instance of Maze with some walls possibly removed
    :param start_row: row coordinate to begin BFS
    :param start_col: col coordinate to begin BFS
    :return: True if all cells are reachable, False otherwise
    """
    rows, cols = maze.rows, maze.cols
    visited = [[False]*cols for _ in range(rows)]

    def get_neighbors(r, c):
        """
        Return a list of adjacent cells (nr, nc) we can move to,
        given that there's no wall blocking the path between (r,c) and (nr,nc).
        """
        neighbors = []

        # Up neighbor
        if r > 0 and not maze.grid[r][c]["up"] and not maze.grid[r-1][c]["down"]:
            neighbors.append((r-1, c))
        # Right neighbor
        if c < cols-1 and not maze.grid[r][c]["right"] and not maze.grid[r][c+1]["left"]:
            neighbors.append((r, c+1))
        # Down neighbor
        if r < rows-1 and not maze.grid[r][c]["down"] and not maze.grid[r+1][c]["up"]:
            neighbors.append((r+1, c))
        # Left neighbor
        if c > 0 and not maze.grid[r][c]["left"] and not maze.grid[r][c-1]["right"]:
            neighbors.append((r, c-1))

        return neighbors

    # BFS starting from (start_row, start_col)
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    visited_count = 1

    while queue:
        cr, cc = queue.popleft()
        for nr, nc in get_neighbors(cr, cc):
            if not visited[nr][nc]:
                visited[nr][nc] = True
                visited_count += 1
                queue.append((nr, nc))

    return visited_count == rows * cols


