
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited_order = []

    visited.add(start)

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return visited_order