"""
Implements a DFS-based approach to "carve" passages in a Maze,
ensuring there's exactly one connected component (i.e., solvable by design).
"""

import random
from maze_lib.maze_representation import Maze, UP, RIGHT, DOWN, LEFT
from collections import deque



def generate_maze_dfs(maze: Maze, start_row: int = 0, start_col: int = 0) -> None:
    rows, cols = maze.rows, maze.cols
    visited = [[False] * cols for _ in range(rows)]

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    directions = [
        (-1, 0, UP, DOWN),     # Move Up
        (0, 1, RIGHT, LEFT),   # Move Right
        (1, 0, DOWN, UP),      # Move Down
        (0, -1, LEFT, RIGHT),  # Move Left
    ]

    def dfs(r: int, c: int) -> None:
        visited[r][c] = True
        random.shuffle(directions)

        for dr, dc, wall_here, wall_there in directions:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and not visited[nr][nc]:
                # Remove walls between current and neighbor
                maze.grid[r, c].remove_wall(wall_here)
                maze.grid[nr, nc].remove_wall(wall_there)
                dfs(nr, nc)

    dfs(start_row, start_col)


def check_maze_connectivity(maze: Maze, start_row: int = 0, start_col: int = 0) -> bool:
    rows, cols = maze.rows, maze.cols
    visited = [[False] * cols for _ in range(rows)]

    def get_neighbors(r: int, c: int) -> list[tuple[int, int]]:
        neighbors = []

        if r > 0 and not maze.grid[r, c].has_wall(UP):
            neighbors.append((r - 1, c))
        if c < cols - 1 and not maze.grid[r, c].has_wall(RIGHT):
            neighbors.append((r, c + 1))
        if r < rows - 1 and not maze.grid[r, c].has_wall(DOWN):
            neighbors.append((r + 1, c))
        if c > 0 and not maze.grid[r, c].has_wall(LEFT):
            neighbors.append((r, c - 1))

        return neighbors

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


