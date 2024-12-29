# Description:
#
# You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely comprised of odd integers or entirely
# comprised of even integers except for a single integer N. Write a method that takes the
# array as an argument and returns N.
#
# For example:
#
# [2, 4, 0, 100, 4, 11, 2602, 36]
#
# Should return: 11
#
# [160, 3, 1719, 19, 11, 13, -21]
#
# Should return: 160
def find_outlier(integers):
    a1 = [n % 2 for n in integers]
    return integers[a1.index(1)] if a1.count(1) == 1 else integers[a1.index(0)]


# def find_outlier(int):
#     odds = [x for x in int if x % 2 != 0]
#     evens = [x for x in int if x % 2 == 0]
#     return odds[0] if len(odds) < len(evens) else evens[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
