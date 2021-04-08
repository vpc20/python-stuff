EMPTY = -9
VISITED = 3


# knight's tour on a n x n board
def knight_tour_recur(n):
    def _knight_tour_recur(x, y, move):
        xy_delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        if move == len(board) ** 2 - 1:
            # return True
            print('-' * 64)
            for r in board:
                # print(r)
                for e in r:
                    print(str(e).zfill(2) + ' ', end='')
                print()
            boards.append(board)
        for xd, yd in xy_delta:
            if -1 < x + xd < n and -1 < y + yd < n and board[x + xd][y + yd] == EMPTY:
                board[x + xd][y + yd] = move + 1
                if _knight_tour_recur(x + xd, y + yd, move + 1):
                    return True
                board[x + xd][y + yd] = EMPTY
        return False

    # board = [[EMPTY] * n for _ in range(n)]
    # board[0][0] = 0
    # _knight_tour_recur(0, 0, 0)

    boards = []
    for x in range(n):
        for y in range(n):
            board = [[EMPTY] * n for _ in range(n)]
            board[x][y] = 0
            print(f'_knight_tour_recur({x}, {y}, 0)')
            _knight_tour_recur(x, y, 0)
            print(len(boards))
    return boards


# def knight_tour_iter(n):
#     board = [[EMPTY] * n for _ in range(n)]
#     # for e in board:
#     #     print(e)
#     x, y = 0, 0
#     stack = [(x, y)]
#     move_count = 0
#     board[x][y] = move_count
#     xy_delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
#     visited = {}
#
#     while stack:
#         for xd, yd in xy_delta:
#             if -1 < x + xd < n and -1 < y + yd < n and board[x + xd][y + yd] == EMPTY:
#                 if move_count + 1 in visited.keys():
#                     list_vxvy = visited[move_count + 1]
#                     for vx, vy in list_vxvy:
#                         if x + xd == vx or y + yd == vy:
#                             continue
#                 move_count += 1
#                 x = x + xd
#                 y = y + yd
#                 board[x][y] = move_count
#                 if move_count == (n * n) - 1:
#                     return board
#                 else:
#                     stack.append((x, y))
#                     try:
#                         visited[move_count].append((x, y))
#                     except KeyError:
#                         visited[move_count] = []
#                         visited[move_count].append((x, y))
#                 print(move_count)
#                 break
#         else:
#             x, y = stack.pop()
#             board[x][y] = EMPTY
#             x = stack[-1][0]
#             y = stack[-1][1]
#             move_count -= 1


# def knight_tour_iter(n):
#     board = [[EMPTY] * n for _ in range(n)]
#     # for e in board:
#     #     print(e)
#     x, y = 0, 0
#     stack = [(x, y)]
#     move_count = 0
#     board[x][y] = move_count
#     visited = {}
#     xy_delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
#
#     while stack:
#         for xd, yd in xy_delta:
#             if -1 < x + xd < n and -1 < y + yd < n and board[x + xd][y + yd] == EMPTY:
#                 if move_count + 1 in visited.keys():
#                     list_vxvy = visited[move_count + 1]
#                     already_visited = False
#                     for vx, vy in list_vxvy:
#                         if x + xd == vx and y + yd == vy:
#                             already_visited = True
#                     if already_visited:
#                         continue
#                 move_count += 1
#                 x = x + xd
#                 y = y + yd
#                 board[x][y] = move_count
#                 stack.append((x, y))
#                 print(board)
#                 if move_count == (n * n) - 1:
#                     return board
#                 if move_count in visited.keys():
#                     visited[move_count].append((x, y))
#                 else:
#                     visited[move_count] = []
#                     visited[move_count].append((x, y))
#                 break
#         else:
#             x, y = stack.pop()
#             board[x][y] = EMPTY
#             move_count -= 1
#     return board


def knight_tour_iter(n):
    board = [[EMPTY] * n for _ in range(n)]
    # for e in board:
    #     print(e)
    x, y = 0, 0
    stack = [(x, y)]
    move_count = 0
    board[x][y] = move_count
    visited = {}
    xy_delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

    while stack:
        for xd, yd in xy_delta:
            if -1 < x + xd < n and -1 < y + yd < n and board[x + xd][y + yd] == EMPTY:
                if move_count + 1 in visited.keys():
                    list_vxvy = visited[move_count + 1]
                    already_visited = False
                    for vx, vy, stck in list_vxvy:
                        if x + xd == vx and y + yd == vy and stack + [(x, y)] == stck:
                            already_visited = True
                    if already_visited:
                        continue
                move_count += 1
                x = x + xd
                y = y + yd
                board[x][y] = move_count
                stack.append((x, y))
                print(move_count)
                if move_count == (n * n) - 1:
                    return board
                # if move_count in visited.keys():
                #     visited[move_count].append((x, y, stack.copy()))
                # else:
                #     visited[move_count] = (x, y, stack.copy())
                if move_count in visited.keys():
                    visited[move_count].append((x, y, stack.copy()))
                else:
                    visited[move_count] = []
                    visited[move_count].append((x, y, stack.copy()))
                break
        else:
            x, y = stack.pop()
            board[x][y] = EMPTY
            move_count -= 1
    return board


if __name__ == '__main__':
    print(len(knight_tour_recur(8)))
    # for row in knight_tour_recur(5):
    #     print(row)

    # no of knight tour in 5x5 board starting from 0,0 to 4,4
    # arr = [304, 304, 360, 360, 664, 664, 720, 720, 776, 776, 832, 832, 896, 896, 952, 952, 1008, 1008,
    #        1064, 1064, 1368, 1368, 1424, 1424, 1728]
    # print([arr[0]] +[arr[i + 1] - arr[i] for i in range(len(arr) - 1)])
    #  304   304   360   360   664
    #  664   720   720   776   776
    #  832   832   896   896   952
    #  952  1008  1008  1064  1064
    # 1368  1368  1424  1424  1728

    # print(knight_tour_iter(5))
    # for row in knight_tour(5):
    #     print(row)
