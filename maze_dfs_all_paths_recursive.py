def print_path_in_maze(maze, path):
    """Visualize the path in the maze"""
    # Create a copy of the maze for visualization
    vis_maze = [row[:] for row in maze]

    # Mark the path with steps number
    steps = 0
    for row, col in path:
        steps += 1
        vis_maze[row][col] = str(steps)

    for row in vis_maze:
        print(*row, sep='\t')
    print()


def maze_to_matrix(maze_str):
    """
    Converts a string representation of a maze into a 2D matrix.

    Args:
      maze_str: The string representation of the maze.

    Returns:
      A 2D list representing the maze.
    """
    rows = maze_str.count('\n') + 1
    x = maze_str.split('\n')
    cols = len(maze_str.split('\n')[0])
    maze_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(maze_str[i * (cols + 1) + j])
        maze_matrix.append(row)
    return maze_matrix


def find_start_end(maze_matrix):
    """
    Finds the starting and ending positions in the maze matrix.

    Args:
      maze_matrix: A 2D list representing the maze.

    Returns:
      A tuple containing the starting and ending positions as tuples (row, col).
    """
    start = None
    end = None
    rows = len(maze_matrix)
    cols = len(maze_matrix[0])

    for row in range(rows):
        for col in range(cols):
            if maze_matrix[row][col] == 'S':
                start = (row, col)
            elif maze_matrix[row][col] == 'E':
                end = (row, col)

    return start, end


def dfs_all_paths(maze_matrix, start, end):
    """
    Performs Depth-First Search (DFS) to find all possible paths through a maze.

    Args:
      maze_matrix: A 2D list representing the maze.
      start: A tuple (row, col) representing the starting position.
      end: A tuple (row, col) representing the ending position.

    Returns:
      A list of lists, where each inner list represents a path found.
    """

    rows, cols = len(maze_matrix), len(maze_matrix[0])
    visited = set()
    all_paths = []

    def dfs_helper(row, col, path):
        if (row, col) == end:
            all_paths.append(path + [(row, col)])
            return

        visited.add((row, col))

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and maze_matrix[new_row][new_col] in ('.', 'E'):
                dfs_helper(new_row, new_col, path + [(row, col)])

        visited.remove((row, col))  # Backtrack

    dfs_helper(start[0], start[1], [])
    return all_paths


#     maze_str = '''.S....
# ##.#..
# ....#.
# #.#...
# ..#...
# .#....
# ..#...
# ....E.'''

maze_str = '''S..
...
..E'''

# maze_str = '''S..
# .#.
# ..E'''

# maze_str = '''S#.
# ...
# ..E'''

maze_matrix = maze_to_matrix(maze_str)
start, end = find_start_end(maze_matrix)

if start is None or end is None:
    print("Start or end position not found in the maze.")
else:
    path = dfs_all_paths(maze_matrix, start, end)

    if start is None or end is None:
        print("Start or end position not found in the maze.")
    else:
        all_paths = dfs_all_paths(maze_matrix, start, end)

        if all_paths:
            print("All paths found:")
            for path in all_paths:
                print(path)
                print_path_in_maze(maze_matrix, path)
        else:
            print("No path found.")
