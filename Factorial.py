from functools import lru_cache


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# def factorial(n):
#     f = 1
#     i = 1
#     while i <= n:
#         f *= i
#         i += 1
#     return f

# recursive - top-down approach
# @lru_cache(maxsize=1000)
# def factorial(n):
#     if n in [0, 1]:
#         return 1
#     return n * factorial(n - 1)


# iterative - bottom-up approach - dynamic programming
# def factorial(n):
#     arr = [1, 1] + [0] * (n - 1)
#     for i in (range(2, n + 1)):
#         arr[i] = i * arr[i - 1]
#     return arr[-1]


# from functools import reduce
#
#
# def factorial(n):
#     return 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))
    # print(factorial(100))
    # print(factorial(1000))
    # # print(factorial(10000))
    #
    # # print(reduce(lambda x, y: x + y, [1, 2, 3]))
