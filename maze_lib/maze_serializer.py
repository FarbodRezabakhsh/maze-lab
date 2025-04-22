
from typing import Dict, List, Tuple
from maze_lib.maze_representation import Maze, UP, RIGHT, DOWN, LEFT

Coord = Tuple[int, int]

def to_graph(maze: Maze) -> Dict[Coord, List[Coord]]:
    graph: Dict[Coord, List[Coord]] = {}
    for r in range(maze.rows):
        for c in range(maze.cols):
            nbrs: List[Coord] = []
            cell = maze.grid[r, c]
            if not cell.has_wall(UP) and r > 0:      nbrs.append((r - 1, c))
            if not cell.has_wall(RIGHT) and c < maze.cols - 1:  nbrs.append((r, c + 1))
            if not cell.has_wall(DOWN) and r < maze.rows - 1:   nbrs.append((r + 1, c))
            if not cell.has_wall(LEFT) and c > 0:     nbrs.append((r, c - 1))
            graph[(r, c)] = nbrs
    return graph
