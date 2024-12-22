def print_path_in_maze(maze, path):
    """Visualize the path in the maze"""
    # Create a copy of the maze for visualization
    vis_maze = [row for row in maze]

    # Mark the path with steps number
    steps = 0
    for row, col in path:
        steps += 1
        vis_maze[row][col] = str(steps)

    for row in vis_maze:
        print(*row, sep='\t')
    print()


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


def dfs(maze, start, end):
    """
    Performs Depth-First Search (DFS) to find a path through a maze.

    Args:
      maze: A 2D list representing the maze.
      start: A tuple (row, col) representing the starting position.
      end: A tuple (row, col) representing the ending position.

    Returns:
      A list of tuples representing the path found, or None if no path exists.
    """

    rows, cols = len(maze), len(maze[0])
    visited = set()
    stack = [(start, [])]

    while stack:
        (row, col), path = stack.pop()

        if (row, col) == end:
            return path + [(row, col)]

        visited.add((row, col))

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Use the specified order
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and maze[new_row][new_col] in ('.', 'E'):
                stack.append(((new_row, new_col), path + [(row, col)]))

    return None


#     maze_str = '''.S....
# ##.#..
# ....#.
# #.#...
# ..#...
# .#....
# ..#...
# ....E.'''

# maze_str = '''S..
# ...
# ..E'''

# maze_str = '''S..
# .#.
# ..E'''

maze_str = '''S#.
...
..E'''

maze = [[c for c in s] for s in maze_str.strip().split('\n')]
start, end = find_start_end(maze)

print('Maze')
for e in maze:
    print(*e, sep='\t')
print()

if start is None or end is None:
    print("Start or end position not found in the maze.")
else:
    path = dfs(maze, start, end)
    if path:
        print(f"Path found: {path}\n")
        print_path_in_maze(maze, path)
    else:
        print("No path found.")
