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
# def x(n):
#     arr1 = []
#     for i in range(n):
#         arr2 = []
#         x = -99
#         for j in range(n):
#             if j == i:
#                 arr2.append(1)
#                 x = n - j - 1
#             else:
#                 if j == x:
#                     arr2.append(1)
#                 else:
#                     arr2.append(0)
#         print arr2

# def x(n):
#     arr1 = []
#     for i in range(n):
#         arr2 = []
#         for j in range(n):
#             if j == i or j == n - i - 1:
#                 arr2.append(1)
#             else:
#                 arr2.append(0)
#         arr1.append(arr2)
#     return arr1

# def x(n):
#     arr = [1 if j == i or j == n - i - 1 else 0 for i in range(n) for j in range(n)]
#     return [arr[i * n:i * n + n] for i in range(n)]

# def x(n):
#     return [[1 if j == i or j == n - i - 1 else 0 for i in range(n)] for j in range(n)]

# def x(n):
#     return [[int(j == i or j == n - i - 1) for i in range(n)] for j in range(n)]

# def x(n):
#     d = [[0] * n for i in range (n)]
#     for i in range(n):
#         d[i][i] = 1
#         d[i][-i-1] = 1
#     return d

# def fill(i, j, n):
#     if i == j or i + j == n - 1:
#        return 1
#     else:
#        return 0
#
# def x(n):
#     return [[fill(i, j, n) for j in range(n)] for i in range(n)]

# def x(n):
#     return [[int(x == y or x == n - y - 1) for x in xrange(n)] for y in xrange(n)]


def x(n):
    output = []
    for i in range(n):
        inner_arr = []
        for j in range(n):
            if i == j or i == n - 1 - j:
                inner_arr.append(1)
            else:
                inner_arr.append(0)
        output.append(inner_arr)
        print(inner_arr)
    return output


# def x(n):
#     return [[1 if i == j or i == n - j - 1 else 0 for i in range(n)] for j in range(n)]


# print x(1)
# print x(2)
# print x(3)
# print x(4)
print(x(5))

# [[1, 0, 0, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 1, 0, 0],
#  [0, 1, 0, 1, 0],
#  [1, 0, 0, 0, 1]]
