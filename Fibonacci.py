# def fib(n):
#     curr, nxt = 0, 1
#     for i in range(n):
#         curr, nxt = nxt, curr + nxt
#     return curr


# def fib(n):
#     prev, curr = 0, 1
#     for i in range(2, n + 1):
#         prev, curr = curr, prev + curr
#     return curr if n > 1 else n


def fib(n):
    fn2, fn1 = 0, 1
    for i in range(2, n + 1):
        f = fn1 + fn2
        fn2, fn1 = fn1, fn1 + fn2
    return f if n > 1 else n


# iterative - bottom-up - dynamic
# def fib(n):
#     arr = [0, 1] + [0] * (n - 1)
#     for i in range(2, n + 1):
#         arr[i] = arr[i - 1] + arr[i - 2]
#     return arr[n]


# def fib(n):
#     if n in [0, 1]:
#         return n
#     return fib(n - 1) + fib(n - 2)


# recursive - memoized
# def fib(n, fib_dict={}):
#     if n in [0, 1]:
#         return n
#     if n in fib_dict:
#         return fib_dict[n]
#     else:
#         fib_dict[n] = fib(n - 1) + fib(n - 2)
#         return fib_dict[n]


# recursive - memoized
# def fib(n):
#     fib_arr = [0, 1] + [0] * (n - 1)
#     return fibx(n, fib_arr)
#
#
# def fibx(n, fib_arr):
#     if n in [0, 1]:
#         return n
#     if fib_arr[n] != 0:
#         return fib_arr[n]
#     fib_arr[n] = fibx(n - 1, fib_arr) + fibx(n - 2, fib_arr)
#     return fib_arr[n]


# recursive - memoized
# def fib(n, fib_results=[0, 1]):
#     if n in [0, 1]:
#         return n
#     if len(fib_results) < n:
#         fib_results.append(fib(n - 1, fib_results))
#     return fib_results[n - 1] + fib_results[n - 2]

# memoized
# def fib(n):
#     fib_arr = [0, 1] + [None] * (n - 2)
#     return fibx(n, fib_arr)
#
#
# def fibx(n, fib_results):
#     if n in [0, 1]:
#         return n
#     if fib_results[n - 1] is None:
#         fib_results[n - 1] = fibx(n - 1, fib_results)
#     if fib_results[n - 2] is None:
#         fib_results[n - 2] = fibx(n - 2, fib_results)
#     return fib_results[n - 1] + fib_results[n - 2]

if __name__ == '__main__':
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(50))
