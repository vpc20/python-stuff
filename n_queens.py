from itertools import permutations, combinations


def validate_full_board(board):
    n = len(board)
    for i in range(n):
        if len(set(board[i])) != 2:
            return False
        if not all([item in [0, 1] for item in board[i]]):
            return False
        if board[i].count(1) != 1:
            return False

    transposed = [[board[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        if len(set(transposed[i])) != 2:
            return False
        if not all([item in [0, 1] for item in transposed[i]]):
            return False
        if transposed[i].count(1) != 1:
            return False

    return True


def valid_board(board, row, col):
    col_delta = 0
    for i in range(row - 1, -1, -1):  # check previous rows
        if board[i][col] == 1:  # check queens in the same column going up
            return False

        # check diagonals
        col_delta += 1

        col_upleft = col - col_delta
        if col_upleft > -1:
            # print(row, diagcolleft)
            if board[i][col_upleft] == 1:
                return False

        col_upright = col + col_delta
        if col_upright < len(board):
            # print(row, diagcolright)
            if board[i][col_upright] == 1:
                return False

    return True


def nqueens(n):
    def _nqueens(row):
        if row == len(board):
            return True
        for col in range(len(board)):
            board[row][col] = 1
            if valid_board(board, row, col):
                if _nqueens(row + 1):
                    return board
            board[row][col] = 0
        return False

    board = [[0] * n for _ in range(n)]
    return _nqueens(0)


def nqueens_iterative(n):
    board = [[0] * n for _ in range(n)]
    row = 0
    col = 0
    stack = []

    while row < n:
        while col < n:
            board[row][col] = 1
            if valid_board(board, row, col):
                if row == len(board):
                    return board
                stack.append(row, col)
                row += 1
                col = 0
                continue
            board[row][col] = 0
            col += 1
    return board


# def nqueens(n):
#     def _nqueens(board, row):
#         if row == len(board):
#             return True
#         for col in range(len(board)):
#             if valid_board(board, row, col):
#                 board[row][col] = 1
#                 if _nqueens(board, row + 1):
#                     return True
#                 board[row][col] = 0
#         return False
#
#     board = [[0] * n for _ in range(n)]
#     _nqueens(board, 0)
#     return board


def nqueens_iter(n):
    board = [[0] * n for _ in range(n)]
    stack = []
    row, col = 0, 0

    while row < len(board):
        while col < len(board):
            if valid_board(board, row, col):
                board[row][col] = 1
                if row == n - 1:  # all n queens completed
                    return board
                stack.append((row, col))
                row += 1
                col = 0
                break
            col += 1
        else:
            row, col = stack.pop()  # backtrack to prev col
            board[row][col] = 0
            if not stack:
                return board  # no solution found
            if col == len(board) - 1:  # exhausted all col
                row, col = stack.pop()  # backtrack to prev row
                board[row][col] = 0
            col += 1


# def is_solution(perm):
#     for i1, i2 in combinations(range(len(perm)), 2):
#         if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
#             return False
#     return True
#
#
# def nqueens_brute(n):
#     for perm in permutations(range(n)):
#         print(perm)
#         if is_solution(perm):
#             board = [[0 for _ in range(n)] for _ in range(n)]
#             for x, y in list(zip(list(range(n)), list(perm))):
#                 board[x][y] = 1
#             for item in board:
#                 print(item)
#             print('')


def is_solution(qcoords):  # check diagonals only
    for i1, i2 in combinations(qcoords, 2):
        if abs(i1[0] - i2[0]) == abs(i1[1] - i2[1]):
            return False
    return True


def nqueens_brute(n):
    for perm in permutations(range(n)):  # permutation of columns
        qcoords = list(zip(list(range(n)), list(perm)))
        if is_solution(qcoords):
            board = [[0 for _ in range(n)] for _ in range(n)]
            for x, y in qcoords:
                board[x][y] = 1
            for item in board:
                print(item)
            print('')


# qarr = [(6, 1), (7, 0)]
# print(valid_board(qarr))
# print(nqueens(4))

# print(nqueens(4))
for e in nqueens(4):
    print(e)
# print(nqueens_iterative(4))
# print('')
# for e in nqueens_iter(4):
#     print(e)

# for i in range(1, 15):
#     print(nqueens(i) == nqueens_iter(i))

print('')
# nqueens_brute(4)
