import sys
import os

# Force Python to see the project root directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from maze_lib.graph_traversal import bfs

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A','D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B','F'],
        'F': ['C','E'],
    }

    start_node = 'A'

    print(f"Starting BFS from node: '{start_node}' ...\n")

    visited_order = bfs(graph, start_node)
    print('BFS visiting order:', visited_order)

if __name__ == '__main__':
    main()