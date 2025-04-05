# Maze Generator & Validator
This project provides a maze generator and optional connectivity validator in Python, ensuring that each generated maze is solvable without needing to store or display the actual solution path.
It also includes BFS and ASCII rendering components, plus a command-line interface (CLI) to manage various tasks (generate, validate, and render the maze).

## Features
1- BFS Warm-Up

- A simple BFS demo (bfs_demo.py) to refresh algorithmic thinking.

2- Maze Representation

- A Maze class (maze_representation.py) storing rows, columns, and the walls of each cell.

- Initially, each cell is fully enclosed by walls (up/down/left/right = True).

3- Maze Generation

- A DFS-based backtracking algorithm (generate_maze_dfs) removes walls to form a single connected “tree” of passages, guaranteeing solvability.

- Stored in maze_generation.py.

4- Connectivity Check (Validation)

- A lightweight BFS approach (check_maze_connectivity) confirms that all cells are reachable from one start cell (e.g., (0,0)), thus validating solvability.

- Located in maze_generation.py (or optionally maze_validation.py).

5- ASCII Rendering

- render_ascii method in the Maze class prints the maze in a text-based format for quick visualization.

5 -Command-Line Interface (CLI)

- A single script maze_cli.py (in scripts/) that uses argparse with three subcommands:

--generate: Create a maze of --rows x --cols.

--validate: Check if that newly generated maze is connected (thus solvable).

--render: Print an ASCII representation to the console.

## Installation
1- ```git clone https://github.com/yourusername/maze-lab.git```
2- ```cd maze-lab```

- Install Dependencies:
- Currently, there’s no external library requirement for basic usage. It’s pure Python.
- pip install --upgrade pip

Command-Line Interface
Run the main CLI script from the project root:
python scripts/maze_cli.py [subcommand] [options]

Subcommands:
- Generate: ```python scripts/maze_cli.py generate --rows 5 --cols 5```
- Validate: ```python scripts/maze_cli.py validate --rows 5 --cols 5```
- Render: ```python scripts/maze_cli.py render --rows 5 --cols 5```

Individual Scripts:
- bfs_demo.py: A warm-up BFS demonstration on a small, hard-coded adjacency list.
- initialize_maze.py: Shows how to instantiate a Maze of given size.
- generate_maze.py: Builds and partially prints info about the generated maze.
- validate_maze.py: Specifically checks if the Maze is fully connected.
- render_maze.py: ASCII output of the Maze structure.