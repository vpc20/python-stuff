EMPTY_CELL = 0
WALL = 1
TARGET_CELL = 2
VISITED = 3


# def search(maze, row, col):
#     if maze[row][col] == TARGET_CELL:
#         print('Target found at', row, col)
#         return True
#     elif maze[row][col] == EMPTY_CELL:
#         print('Visiting cell', row, col)
#         maze[row][col] = VISITED
#
#     if row - 1 > -1 and maze[row - 1][col] in [EMPTY_CELL, TARGET_CELL]:
#         if search(maze, row - 1, col):
#             return True
#     if col + 1 <= len(maze) - 1 and maze[row][col + 1] in [EMPTY_CELL, TARGET_CELL]:
#         if search(maze, row, col + 1):
#             return True
#     if row + 1 <= len(maze) - 1 and maze[row + 1][col] in [EMPTY_CELL, TARGET_CELL]:
#         if search(maze, row + 1, col):
#             return True
#     if col - 1 > -1 and maze[row][col - 1] in [EMPTY_CELL, TARGET_CELL]:
#         if search(maze, row, col - 1):
#             return True
#     return False


def search(maze, row, col):
    if maze[row][col] == TARGET_CELL:
        print('Target found at', row, col)
        return True
    elif maze[row][col] == EMPTY_CELL:
        print('Visiting cell', row, col)
        maze[row][col] = VISITED
    else:
        return False

    if row - 1 > -1 and search(maze, row - 1, col) \
            or col + 1 < len(maze) and search(maze, row, col + 1) \
            or row + 1 < len(maze) and search(maze, row + 1, col) \
            or col - 1 > -1 and search(maze, row, col - 1):
        return True


# def search(maze, row, col):
#     if maze[row][col] == TARGET_CELL:
#         print('found at %d,%d' % (row, col))
#         return True
#     elif maze[row][col] == WALL:
#         print('wall at %d,%d' % (row, col))
#         return False
#     elif maze[row][col] == VISITED:
#         print('visited at %d,%d' % (row, col))
#         return False
#
#     print('visiting %d,%d' % (row, col))
#
#     # mark as visited
#     maze[row][col] = VISITED
#
#     # explore neighbors clockwise starting by the one on the right
#     if ((row < len(maze) - 1 and search(maze, row + 1, col))
#         or (col < len(maze) - 1 and search(maze, row, col + 1))
#         or (col > 0 and search(maze, row, col - 1))
#         or (row > 0 and search(maze, row - 1, col))):
#         return True
#
#     return False


# maze = [[0, 0, 0, 0, 0, 1],
#         [1, 1, 0, 0, 0, 1],
#         [0, 0, 0, 1, 0, 0],
#         [0, 1, 1, 0, 0, 1],
#         [0, 1, 0, 0, 1, 0],
#         [0, 1, 0, 0, 0, 2]]

def maze_recur(maze, startx, starty):
    def _maze_recur(x, y):
        xy_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for xd, yd in xy_delta:
            if -1 < x + xd < len(maze) and -1 < y + yd < len(maze):
                if maze[x + xd][y + yd] == TARGET_CELL:
                    return True
                if maze[x + xd][y + yd] == EMPTY_CELL:
                    maze[x + xd][y + yd] = VISITED
                    if _maze_recur(x + xd, y + yd):
                        return True
                    maze[x + xd][y + yd] = EMPTY_CELL
        return False

    _maze_recur(startx, starty)
    return maze


# maze1 = [[1, 1, 0, 1, 0, 2],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0],
#         [0, 1, 0, 1, 1, 1],
#         [0, 1, 0, 0, 0, 0]]
maze1 = [[1, 1, 0, 1, 0, 2],
         [0, 1, 0, 0, 1, 0],
         [0, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [0, 0, 0, 0, 0, 0]]

# print(search(maze, 5, 0))
# for e in maze:
#     print(e)

print(maze_recur(maze1, 5, 0))
