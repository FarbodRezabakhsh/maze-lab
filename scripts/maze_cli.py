# scripts/maze_cli.py
import sys
import os
import argparse
import random

# Raise recursion limit if you want bigger mazes with recursive DFS
sys.setrecursionlimit(10_000)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from maze_lib.maze_representation import Maze
from maze_lib.maze_generation import generate_maze_dfs, check_maze_connectivity
from maze_lib.maze_io import save_maze, load_maze
from maze_lib.maze_serializer import to_graph
from maze_lib.maze_solver import solve_backtrack, path_to_directions



def generate_command(args):
    """
    Subcommand: Generate a maze of given rows x cols.
    Optionally save it to a file (--output).
    """
    maze = Maze(args.rows, args.cols)
    if args.seed is not None:
        random.seed(args.seed)
    generate_maze_dfs(maze, 0, 0)

    print(f"Generated a {args.rows}x{args.cols} maze (DFS).")
    if args.output:
        save_maze(maze, args.output)
        print(f"Saved maze to {args.output}.")


def validate_command(args):
    """
    Subcommand: Validate a newly generated or loaded maze is fully connected.
    If --input is provided, load from file; otherwise generate a fresh Maze.
    """
    if args.input:
        # Load from file
        maze = load_maze(args.input)
        print(f"Loaded maze from {args.input}.")
    else:
        # Generate new Maze in memory
        maze = Maze(args.rows, args.cols)
        if args.seed is not None:
            random.seed(args.seed)
        generate_maze_dfs(maze, 0, 0)
        print(f"Generated a {args.rows}x{args.cols} maze (DFS) in memory.")

    is_connected = check_maze_connectivity(maze, 0, 0)
    if is_connected:
        print("Maze is fully connected (solvable).")
    else:
        print("Maze is NOT fully connected. Some cells are isolated.")


def render_command(args):
    """
    Subcommand: Render a maze in ASCII, either loaded from file or newly generated.
    """
    if args.input:
        maze = load_maze(args.input)
        print(f"Loaded maze from {args.input}.")
    else:
        maze = Maze(args.rows, args.cols)
        if args.seed is not None:
            random.seed(args.seed)
        generate_maze_dfs(maze, 0, 0)
        print(f"Generated a {args.rows}x{args.cols} maze in memory.")

    print("ASCII representation:\n")
    maze.render_ascii()

def solve_command(args: argparse.Namespace) -> None:
    if args.input:
        maze = load_maze(args.input)
        print(f"Loaded maze from {args.input}.")
    else:
        maze = Maze(args.rows, args.cols)
        if args.seed is not None:
            random.seed(args.seed)
        generate_maze_dfs(maze, 0, 0)
        print(f"Generated a {args.rows}×{args.cols} maze in memory.")
    graph = to_graph(maze)
    start, goal = (0, 0), (maze.rows - 1, maze.cols - 1)
    path = solve_backtrack(graph, start, goal)
    dirs = path_to_directions(path)

    print("Path:", " -> ".join(f"{p}" for p in path))
    print("Directions:", ", ".join(dirs))
    print("\nMaze with path overlay:\n")
    maze.render_ascii(path)



def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for Maze tasks: generate, validate, render, or solve."
    )
    parser.add_argument(
        "--seed", type=int,
        help="Optional random seed for reproducibility"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate subcommand
    generate_parser = subparsers.add_parser('generate', help='Generate a solvable maze using DFS.')
    generate_parser.add_argument('--rows', type=int, default=5, help='Number of rows')
    generate_parser.add_argument('--cols', type=int, default=5, help='Number of columns')
    generate_parser.add_argument('--output', type=str, help='File path to save the generated maze (JSON)')
    generate_parser.set_defaults(func=generate_command)

    # validate subcommand
    validate_parser = subparsers.add_parser('validate', help='Check connectivity of a maze.')
    validate_parser.add_argument('--rows', type=int, default=5, help='Number of rows (if no input file)')
    validate_parser.add_argument('--cols', type=int, default=5, help='Number of columns (if no input file)')
    validate_parser.add_argument('--input', type=str,
                                 help='File path to load a Maze (JSON). If not provided, a new Maze is generated.')
    validate_parser.set_defaults(func=validate_command)

    # render subcommand
    render_parser = subparsers.add_parser('render', help='Render a maze in ASCII.')
    render_parser.add_argument('--rows', type=int, default=5, help='Number of rows (if no input file)')
    render_parser.add_argument('--cols', type=int, default=5, help='Number of columns (if no input file)')
    render_parser.add_argument('--input', type=str,
                               help='File path to load a Maze (JSON). If not provided, a new Maze is generated.')
    render_parser.set_defaults(func=render_command)

    solve = subparsers.add_parser("solve", help="Solve a maze and show the path")
    solve.add_argument("--rows", type=int, default=5)
    solve.add_argument("--cols", type=int, default=5)
    solve.add_argument("--input", type=str, help="Path to load maze JSON")
    solve.set_defaults(func=solve_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
