# from functools import lru_cache


def memoize(func):
    def wrapper(k):
        if k in cache:
            return cache[k]
        else:
            cache[k] = func(k)
            return cache[k]

    cache = {}
    return wrapper


# @lru_cache(maxsize=None)
@memoize
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(50))
