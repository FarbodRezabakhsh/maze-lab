import random
from collections import deque
from typing import List, Tuple
from maze_lib.maze_representation import Maze, UP, RIGHT, DOWN, LEFT

def generate_maze_dfs(
    maze: Maze,
    start_row: int = 0,
    start_col: int = 0
) -> None:
    rows, cols = maze.rows, maze.cols
    visited: List[List[bool]] = [[False] * cols for _ in range(rows)]

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    directions: List[Tuple[int, int, int, int]] = [
        (-1, 0, UP, DOWN),
        (0, 1, RIGHT, LEFT),
        (1, 0, DOWN, UP),
        (0, -1, LEFT, RIGHT),
    ]

    def dfs(r: int, c: int) -> None:
        visited[r][c] = True
        random.shuffle(directions)
        for dr, dc, w_here, w_there in directions:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and not visited[nr][nc]:
                maze.grid[r, c].remove_wall(w_here)
                maze.grid[nr, nc].remove_wall(w_there)
                dfs(nr, nc)

    dfs(start_row, start_col)

def check_maze_connectivity(
    maze: Maze,
    start_row: int = 0,
    start_col: int = 0
) -> bool:
    rows, cols = maze.rows, maze.cols
    visited: List[List[bool]] = [[False] * cols for _ in range(rows)]

    def get_neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        nbrs: List[Tuple[int, int]] = []
        if r > 0 and not maze.grid[r, c].has_wall(UP):
            nbrs.append((r - 1, c))
        if c < cols - 1 and not maze.grid[r, c].has_wall(RIGHT):
            nbrs.append((r, c + 1))
        if r < rows - 1 and not maze.grid[r, c].has_wall(DOWN):
            nbrs.append((r + 1, c))
        if c > 0 and not maze.grid[r, c].has_wall(LEFT):
            nbrs.append((r, c - 1))
        return nbrs

    queue: deque[Tuple[int, int]] = deque([(start_row, start_col)])
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
