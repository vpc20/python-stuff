from collections import deque


def print_path_in_maze(maze, path):
    """Visualize the path in the maze"""
    # Create a copy of the maze for visualization
    vis_maze = [row[:] for row in maze]

    # Mark the path with '*'
    steps = 0
    for row, col in path:
        steps += 1
        vis_maze[row][col] = str(steps)

    for row in vis_maze:
        print(*row, sep='\t')
    print()


def bfs_maze_paths(maze, start, end):
    """
    Finds all possible paths through a maze using Breadth-First Search (BFS).

    Args:
      maze: A 2D list representing the maze.
             0 represents a valid path, 1 represents a wall.
      start: A tuple representing the starting position (row, col).
      end: A tuple representing the ending position (row, col).

    Returns:
      A list of all possible paths, where each path is a list of tuples
      representing the coordinates of the cells visited in the path.
    """

    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])  # Queue to store nodes to be visited
    visited = set()  # Set to keep track of visited nodes (using a set for faster lookups)

    all_paths = []

    while queue:
        (r, c), path = queue.popleft()

        # Check if we have reached the end
        if (r, c) == end:
            all_paths.append(path)
            continue

        # Define possible moves (up, down, left, right)
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
            # Check if the new position is valid (within bounds and not a wall)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                # Only add to the queue if not previously visited in this specific path
                if (nr, nc) not in path:
                    queue.append(((nr, nc), path + [(nr, nc)]))

    # remove duplicates - convert to tuple, then convert to set, then convert to list
    # all_paths_tuple = [tuple(i) for i in all_paths]
    # x = list(set(all_paths_tuple))
    # print(len(all_paths))
    # print(len(x))
    return all_paths


# Example usage
maze_txt = '''
...
...
...'''

# maze_txt = '''
# ...
# .#.
# ...'''

print('Maze')
maze = [[c for c in txt] for txt in maze_txt.strip().split('\n')]
for e in maze:
    print(*e, sep='\t')
print()

start = (0, 0)
end = (2, 2)

all_paths = bfs_maze_paths(maze, start, end)

if all_paths:
    print("All possible paths:")
    for path in all_paths:
        print(path)
        print_path_in_maze(maze, path)
else:
    print("No path found.")
