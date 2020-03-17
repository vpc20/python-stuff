# def replicate(num, n):
#     res = []
#     for i in range(n):
#         res.append(num)
#     return res


# def replicate(num, n):
#     return [num for _ in range(n)]

def replicate(num, n):
    return [num] * n


def replicate_recur(num, n):
    def _replicate_recur(num, n):
        nonlocal arr
        if n == 0:
            return
        arr += [num]
        _ = _replicate_recur(num, n - 1)
        return arr

    arr = []
    return _replicate_recur(num, n)


# def replicate_recur(num, n):
#     return _replicate_recur(num, n, arr=[])
#
#
# def _replicate_recur(num, n, arr=[]):
#     if n == 0:
#         return
#     arr += [num]
#     _ = _replicate_recur(num, n - 1, arr)
#     return arr


# def replicate_recur(num, n, arr=[]): # the function call should always pass []
#     if n == 0:                       # otherwise
#         return [num]
#     _ = replicate_recur(num, n - 1, arr)
#     arr += [num]
#     return arr


print(replicate(5, 1))
print(replicate(5, 2))
print(replicate(5, 3))
print(replicate(5, 4))
print(replicate(5, 5))

print(replicate_recur(5, 1))
print(replicate_recur(5, 2))
print(replicate_recur(5, 3))
print(replicate_recur(5, 4))
print(replicate_recur(5, 5))

# print(replicate_recur(5, 1, []))
# print(replicate_recur(5, 2, []))
# print(replicate_recur(5, 3, []))
# print(replicate_recur(5, 4, []))
# print(replicate_recur(5, 5, []))
