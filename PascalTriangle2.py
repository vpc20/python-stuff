# Given an integer rowIndex, return the rowIndexth(0 - indexed) row of the Pascal 's triangle.
#
# In Pascal 's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
# Input: rowIndex = 3
# Output: [1, 3, 3, 1]
#
# Example 2:
# Input: rowIndex = 0
# Output: [1]
#
# Example 3:
# Input: rowIndex = 1
# Output: [1, 1]
#
# Constraints:
# 0 <= rowIndex <= 33
#
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

from datetime import datetime


def pascal1(n):
    triangle = []
    for i in range(n + 1):
        triangle.append([1 for _ in range(i + 1)])
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
    return triangle[-1]


def pascal2(n):  # faster version
    triangle = [[1]]
    for i in range(n):
        triangle.append([1])
        for j in range(1, i + 1):
            triangle[i + 1].append(triangle[i][j] + triangle[i][j - 1])
        triangle[i + 1].append(1)
    return triangle[-1]


def pascal2a(n):  # fastest, optimized space
    row = [0] * (n + 1)
    row[0] = 1
    for k in range(1, n + 1):
        row[k] = 1
        for i in range(k - 1, 0, -1):
            row[i] += row[i - 1]
    return row


# def pascal2a(n):  # faster version
#     if n == 0:
#         return [1]
#     triangle = [1]
#     for i in range(1, n - 1):
#         triangle[i + 1] = triangle[i + 1] + triangle[i]
#     triangle.append(1)
#     return triangle


print(pascal1(0))
print(pascal2(0))

print(pascal1(1))
print(pascal2(1))

print(pascal1(2))
print(pascal2(2))

print(pascal1(3))
print(pascal2(3))

print(pascal1(4))
print(pascal2(4))

print(pascal1(5))
print(pascal2(5))

print(pascal2a(0))
print(pascal2a(1))
print(pascal2a(2))
print(pascal2a(3))
print(pascal2a(4))

# print(timeit('pascal1(5)', 'from __main__ import pascal1'))
# print(timeit('pascal2(5)', 'from __main__ import pascal2'))

t1 = datetime.now()
for i in range(600):
    pascal1(i)
t2 = datetime.now()
x = t2 - t1
print(x.seconds)

t1 = datetime.now()
for i in range(600):
    pascal2(i)
t2 = datetime.now()
x = t2 - t1
print(x.seconds)

t1 = datetime.now()
for i in range(600):
    pascal2a(i)
t2 = datetime.now()
x = t2 - t1
print(x.seconds)
