# Write a function x(n) that takes in a number n and returns an nxn array with an X
#  in the middle. The X will be represented by 1's and the rest will be 0's.
# E.g.
#
# x(5) ==  [[1, 0, 0, 0, 1],
#           [0, 1, 0, 1, 0],
#           [0, 0, 1, 0, 0],
#           [0, 1, 0, 1, 0],
#           [1, 0, 0, 0, 1]];
#
# x(6) ==  [[1, 0, 0, 0, 0, 1],
#           [0, 1, 0, 0, 1, 0],
#           [0, 0, 1, 1, 0, 0],
#           [0, 0, 1, 1, 0, 0],
#           [0, 1, 0, 0, 1, 0],
#           [1, 0, 0, 0, 0, 1]];


def x(n):
    xarr = [[0] * n for _ in range(n)]
    for i in range(n):
        xarr[i][i] = 1
        xarr[i][n - 1 - i] = 1
    return xarr


for i in range(6):
    arr = x(i)
    for e in arr:
        print(e)
    print('')
