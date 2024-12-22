from collections import deque


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


def bfs_maze_paths(maze, start, end):
    """
    Finds all possible paths through a maze using Breadth-First Search (BFS).

    Args:
      maze: A 2D list representing the maze.
             . represents a valid path, # represents a wall.
      start: A tuple representing the starting position (row, col).
      end: A tuple representing the ending position (row, col).

    Returns:
      One of the possible paths. There could be more solutions or none.
    """

    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])  # Queue to store nodes to be visited

    while queue:
        (r, c), path = queue.popleft()

        # Check if we have reached the end
        if (r, c) == end:
            return path

        # Define possible moves (up, down, left, right)
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
            # Check if the new position is valid (within bounds and not a wall)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                # Only add to the queue if not previously visited in this specific path
                if (nr, nc) not in path:
                    queue.append(((nr, nc), path + [(nr, nc)]))
                # queue.append(((nr, nc), path + [(nr, nc)]))

    return single_path


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

single_path = bfs_maze_paths(maze, start, end)

if single_path:
    print("One of the solution path:")
    print(single_path)
    print_path_in_maze(maze, single_path)
else:
    print("No path found.")
