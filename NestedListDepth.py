# Description:
#
# A nested list (or array in JavaScript) is a list that apears as a value inside another list,
#
# [item, item, [item, item], item]
# in the above list, [item, item] is a nested list.
#
# Your goal is to write a function that determines the depth of the deepest nested list within a given list.
# return 1 if there are no nested lists. The list passed to your function can contain any data types.
#
# A few examples:
#
# list_depth([True])
# return 1
#
# list_depth([])
# return 1
#
# list_depth([2, "yes", [True, False]])
# return 2
#
# list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1])
# return 6
#
# list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]])
# return 2


# recursive solution incorrect
# def list_depth(lst):
#     x = 0
#     for e in lst:
#         if type(e) is list:
#             x = list_depth(e)
#     return 1 + x

# recursive solution
# def list_depth_recur(arr, d=1):
#     # print(arr, d)
#     list_found = False
#     for e in arr:
#         if type(e) is list:
#             list_found = True
#             d = list_depth_recur(e, d)
#     if list_found:
#         d += 1
#     return d

# def list_depth_recur(arr, d=1):
#     for e in arr:
#         if type(e) is list:
#             # x = 1 + list_depth_recur(e, d)
#             d = max(d, list_depth_recur(e, d + 1))
#     return d

def list_depth_recur(arr):
    d = 1
    for e in arr:
        if type(e) is list:
            d = max(d, 1 + list_depth_recur(e))
    return d


# iterative solution
def list_depth_iter(lst):
    level = 1
    queue = [lst]
    while queue:
        list_found = False
        for e in queue[0]:
            if type(e) is list:
                list_found = True
                queue.append(e)
        if list_found:
            level += 1
        queue.pop(0)
    return level


if __name__ == '__main__':
    assert list_depth_iter([1]) == 1
    assert list_depth_iter([1, 2, 3]) == 1
    assert list_depth_iter([[1, 2], 3]) == 2
    assert list_depth_iter([1, [2, 3]]) == 2
    assert list_depth_iter([1, [2, 3, [4]]]) == 3
    assert list_depth_iter([[8, 9], 1, [2, 3, [4]]]) == 3
    assert list_depth_iter([[[[[1]]]]]) == 5

    assert list_depth_iter([1, [2, 2], 1, [2, 2], 1, [2, 2]]) == 2
    assert list_depth_iter([1, 2, 3, 4, 5]) == 1

    assert list_depth_iter([[8, 9], 1, [[1], 2, 3]]) == 3
    assert list_depth_iter([[1, 2], [3, 4]]) == 2
    assert list_depth_iter([[1, 2], [3, 4], [5, 6]]) == 2
    assert list_depth_iter([[1, 2], [3, 4, [1]], [5, 6]]) == 3

    assert list_depth_iter([1, [2]]) == 2
    assert list_depth_iter([[1], 2]) == 2

    assert list_depth_iter([1, [2], [3, [4]]]) == 3
    assert list_depth_iter([[3, [4]], 1, [2]]) == 3
    assert list_depth_iter([[3, [4], 1, [2]]]) == 3
    assert list_depth_iter([[[3]]]) == 3

    assert list_depth_iter([[8, 9], 1, [2, 3, [4]]]) == 3
    assert list_depth_recur([[8, 9], 1, [2, 3, [4]]]) == 3
    assert list_depth_recur([8]) == 1
    assert list_depth_recur([[8, [1]], [7], [6]]) == 3
