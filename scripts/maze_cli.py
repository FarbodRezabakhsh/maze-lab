
import sys
import os
import argparse
import random

# Make sure Python can see the project root (same hack we used before)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from maze_lib.maze_representation import Maze
from maze_lib.maze_generation import generate_maze_dfs, check_maze_connectivity

def generate_command(args):
    """
    Subcommand: Generate a maze of given rows x cols.
    By default, just shows a confirmation message.
    """
    random.seed(42)
    maze = Maze(args.rows, args.cols)
    generate_maze_dfs(maze, 0, 0)

    print(f"Generated a {args.rows}x{args.cols} maze using DFS approach.")
    print("Walls have been removed to ensure it's solvable.")

def validate_command(args):
    """
    Subcommand: Validate a newly generated maze is fully connected.
    """
    random.seed(42)
    maze = Maze(args.rows, args.cols)
    generate_maze_dfs(maze, 0, 0)

    is_connected = check_maze_connectivity(maze, 0, 0)
    if is_connected:
        print(f"The {args.rows}x{args.cols} maze is fully connected (solvable).")
    else:
        print(f"The {args.rows}x{args.cols} maze is NOT fully connected.")

def render_command(args):
    """
    Subcommand: Render an ASCII view of the maze in the console.
    """
    random.seed(42)
    maze = Maze(args.rows, args.cols)
    generate_maze_dfs(maze, 0, 0)

    print(f"Rendering a {args.rows}x{args.cols} maze in ASCII:\n")
    # This requires you have 'render_ascii' in Maze class
    maze.render_ascii()

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for Maze tasks: generate, validate, or render a maze."
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subcommand: generate
    generate_parser = subparsers.add_parser(
        'generate',
        help='Generate a solvable maze using DFS.'
    )
    generate_parser.add_argument('--rows', type=int, default=5, help='Number of rows')
    generate_parser.add_argument('--cols', type=int, default=5, help='Number of columns')

    # Subcommand: validate
    validate_parser = subparsers.add_parser(
        'validate',
        help='Check connectivity (solvability) of a newly generated maze.'
    )
    validate_parser.add_argument('--rows', type=int, default=5, help='Number of rows')
    validate_parser.add_argument('--cols', type=int, default=5, help='Number of columns')

    # Subcommand: render
    render_parser = subparsers.add_parser(
        'render',
        help='Render an ASCII representation of the maze.'
    )
    render_parser.add_argument('--rows', type=int, default=5, help='Number of rows')
    render_parser.add_argument('--cols', type=int, default=5, help='Number of columns')

    # Parse the CLI arguments
    args = parser.parse_args()

    # Dispatch to the correct function based on subcommand
    if args.command == 'generate':
        generate_command(args)
    elif args.command == 'validate':
        validate_command(args)
    elif args.command == 'render':
        render_command(args)

if __name__ == "__main__":
    main()
