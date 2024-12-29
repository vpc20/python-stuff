EMPTY_CELL = 0
WALL = 1
TARGET_CELL = 2
VISITED = 3


def search(maze, row, col):
    stack = [(row, col)]
    while stack:
        if maze[row][col] == TARGET_CELL:
            print('Target found at', row, col)
            return True
        elif maze[row][col] == EMPTY_CELL:
            print('Visiting cell', row, col)
            maze[row][col] = VISITED
            stack.append((row, col))
        else:
            row, col = stack.pop()

        if row - 1 > -1 and maze[row - 1][col] in [EMPTY_CELL, TARGET_CELL]:  # up
            row -= 1
        elif col + 1 < len(maze) and maze[row][col + 1] in [EMPTY_CELL, TARGET_CELL]:  # right
            col += 1
        elif row + 1 < len(maze) and maze[row + 1][col] in [EMPTY_CELL, TARGET_CELL]:  # down
            row += 1
        elif col - 1 > -1 and maze[row][col - 1] in [EMPTY_CELL, TARGET_CELL]:  # left
            col -= 1

    return False


# def maze_iter(maze, x, y):
#     stack = [(x, y)]
#     xy_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     while stack:
#         for xd, yd in xy_delta:
#             if -1 < x + xd < len(maze) and -1 < y + yd < len(maze):
#                 if maze[x + xd][y + yd] == TARGET_CELL:
#                     return maze
#                 if maze[x + xd][y + yd] == EMPTY_CELL:
#                     x = x + xd
#                     y = y + yd
#                     stack.append((x, y))
#                     maze[x][y] = VISITED
#                     break
#         else:
#             _ = stack.pop()
#             x = stack[-1][0]
#             y = stack[-1][1]
#     return maze


def maze_iter(maze, row, col):
    stack = [(row, col)]
    maze[row][col] = VISITED
    while stack:
        for r, c in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
            if -1 < r < len(maze) and -1 < c < len(maze):
                if maze[r][c] == TARGET_CELL:
                    return maze
                if maze[r][c] == EMPTY_CELL:
                    stack.append((row, col))
                    maze[r][c] = VISITED
                    row = r
                    col = c
                    break
        else:
            row, col = stack.pop()
    return False


# def maze_iter(maze, x, y):
#     stack = [(x, y)]
#     maze[x][y] = VISITED
#     xy_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     while stack:
#         for xd, yd in xy_delta:
#             if -1 < x + xd < len(maze) and -1 < y + yd < len(maze):
#                 if maze[x + xd][y + yd] == TARGET_CELL:
#                     return maze
#                 if maze[x + xd][y + yd] == EMPTY_CELL:
#                     stack.append((x, y))
#                     x = x + xd
#                     y = y + yd
#                     maze[x][y] = VISITED
#                     break
#         else:
#             x, y = stack.pop()
#     return maze
#
# def check_maze(maze, row, col):
#     if maze[row][col] == EMPTY_CELL:
#         print 'Visiting cell', row, col
#         maze[row][col] = VISITED
#         stack.append((row, col))
#     elif maze[row][col] == TARGET_CELL:
#         print 'Target found at', row, col
#         return True
#     elif maze[row][col] == WALL:
#         print 'Wall encountered at', row, col
#     elif maze[row][col] == VISITED:
#         print 'Visited cell at', row, col

# def search(maze, row, col):
#     print 'Visiting cell', row, col
#     maze[row][col] = VISITED
#     stack.append((row, col))
#
#     while True:
#         # up
#         if row - 1 > -1 and maze[row - 1][col] != EMPTY_CELL and maze[row - 1][col] != TARGET_CELL:
#             row -= 1
#             if check_maze(maze, row, col):
#                 break
#         # right
#         elif col + 1 < len(maze) - 1 and maze[row][col + 1] != EMPTY_CELL and maze[row][col + 1] != TARGET_CELL:
#             col += 1
#             if check_maze(maze, row, col):
#                 break
#         # down
#         elif row + 1 < len(maze) - 1 and maze[row + 1][col] != EMPTY_CELL and maze[row + 1][col] != TARGET_CELL:
#             row += 1
#             if check_maze(maze, row, col):
#                 break
#         # left
#         elif col - 1 > -1 and maze[row][col - 1] != EMPTY_CELL and maze[row][col - 1] != TARGET_CELL:
#             col -= 1
#             if check_maze(maze, row, col):
#                 break
#         else:
#             x = stack.pop()
#             row = x[0]
#             col = x[1]
#
#
# def check_maze(maze, row, col):
#     if maze[row][col] == EMPTY_CELL:
#         print 'Visiting cell', row, col
#         maze[row][col] = VISITED
#         stack.append((row, col))
#     elif maze[row][col] == TARGET_CELL:
#         print 'Target found at', row, col
#         return True
#     elif maze[row][col] == WALL:
#         print 'Wall encountered at', row, col
#     elif maze[row][col] == VISITED:
#         print 'Visited cell at', row, col

# pop from stack if there are no more paths available in any direction  # maze = [[0, 0, 0, 0, 0, 1],


# maze1 = [[0, 0, 0, 1, 0, 2],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 0, 0, 1]]

# maze1 = [[0, 0, 0, 1, 0, 2],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [1, 1, 1, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0, 1]]
#
# print(search(maze1, 5, 0))
# print(maze1)
# for e in maze1:
#     print(e)

# maze1 = [[0, 0, 0, 1, 0, 2],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 1, 0, 1],
#          [0, 1, 0, 0, 0, 1]]

maze1 = [[0, 0, 0, 1, 0, 2],
         [0, 1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 0, 1],
         [0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 1]]

print(maze_iter(maze1, 5, 0))
for e in maze1:
    print(e)
