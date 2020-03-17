from functools import lru_cache


# can be used to get binomial coefficient
@lru_cache()
def pascal_recur(n, k):
    if k == 0 or k == n:
        return 1
    return pascal_recur(n - 1, k - 1) + pascal_recur(n - 1, k)


def pascal_iter(n, k):  # dynamic solution
    # dp_arr = [[1] + [0 for _ in range(k)] for _ in range(n + 1)]
    dp_arr = [[1] + [0] * k for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp_arr[i][j] = dp_arr[i - 1][j - 1] + dp_arr[i - 1][j]
    for e in dp_arr:
        print(e)
    print(dp_arr)
    return dp_arr[-1][-1]


if __name__ == '__main__':
    print(pascal_recur(5, 5))
    print(pascal_iter(5, 5))
