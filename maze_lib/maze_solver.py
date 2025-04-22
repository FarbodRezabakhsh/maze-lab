

from typing import Dict, List, Tuple
from maze_lib.maze_serializer import to_graph

Coord = Tuple[int, int]

def solve_backtrack(
    graph: Dict[Coord, List[Coord]],
    start: Coord,
    goal: Coord
) -> List[Coord]:
    path: List[Coord] = []
    visited: set[Coord] = set()

    def dfs(node: Coord) -> bool:
        if node == goal:
            path.append(node)
            return True
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited and dfs(nbr):
                path.append(node)
                return True
        return False

    dfs(start)
    return list(reversed(path))


def path_to_directions(path: List[Coord]) -> List[str]:
    dirs: List[str] = []
    for (r0, c0), (r1, c1) in zip(path, path[1:]):
        dr, dc = r1 - r0, c1 - c0
        if (dr, dc) == (-1, 0):
            dirs.append("Up")
        elif (dr, dc) == (1, 0):
            dirs.append("Down")
        elif (dr, dc) == (0, 1):
            dirs.append("Right")
        elif (dr, dc) == (0, -1):
            dirs.append("Left")
    return dirs
