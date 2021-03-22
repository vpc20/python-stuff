def pascal(n):
    triangle = [[1]]
    for i in range(n):
        triangle.append([1])
        for j in range(1, i + 1):
            triangle[i + 1].append(triangle[i][j] + triangle[i][j - 1])
        triangle[i + 1].append(1)
    return triangle


print(pascal(0))  # 0-indexed pascal triangle generations
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
