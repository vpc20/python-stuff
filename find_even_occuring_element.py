# Given an integer array, one element occurs even number of times and all
# others have odd occurrences. Find the first element with even occurrences.

from collections import Counter


def find_even(arr):
    for n, count in Counter(arr).items():
        if count % 2 == 0:
            return n


print(find_even([1, 2, 6, 5, 5, 5, 4, 3, 5]))
