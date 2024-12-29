# In computer science, cycle detection is the algorithmic problem of finding a cycle in a
# sequence of iterated function values.
#
# For any function f, and any initial value x0 in S, the sequence of iterated function values
#
# x0,x1=f(x0), x2=f(x1), ...,xi=f(x{i-1}),...
# may eventually use the same value twice under some assumptions: S finite, f periodic  etc.
# So there will be some i not = j such that xi = xj. Once this happens, the sequence must
# continue by repeating the cycle of values from xi to xj-1. Cycle detection is the problem
# of finding i and j, given f and x0. Let u be the smallest index such that the value
# associated will reappears and l the smallest value such that xuu = xl+u, l is the loop length.
#
# Example:
#
# Consider the sequence: 2, 0, 6, 3, 1, 6, 3, 1, 6, 3, 1, ....
#  The cycle in this value sequence is 6, 3, 1. u is 2 (first 6) l is 3 (length of the sequence
# or difference between position of consecutive 6)
#
# The goal of this kata is to build a function that will return [u,l] when given a short
# sequence. Simple loops will be sufficient. The sequence will be given in the form
# of an array. All array will be valid sequence associated with deterministic function.
# It means that the sequence will repeat itself when a value is reached a second time.
# (So you treat two cases: non repeating [1,2,3,4] and repeating [1,2,1,2], no hybrid
# cases like [1,2,1,4]). If there is no repetition you should return [].

def cycle(seq):
    for i in range(len(seq)):
        for j in range(1, len(seq)):
            arr = seq[i:]
            subarr = seq[i:i + j]
            if len(subarr) <= len(arr):
                if is_cycle(arr, subarr):
                    return [i, i + j - i]
            else:
                break
    return []


def is_cycle(arr, subarr):
    # print arr, subarr
    if len(arr) % len(subarr) != 0:
        return False
    if arr == subarr:
        return False

    i = 0
    while i <= len(arr) - len(subarr):
        for j in range(len(subarr)):
            if subarr[j] == arr[i]:
                i += 1
            else:
                return False
    return True


# print is_cycle([1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3])
# print is_cycle([1, 2, 1, 2, 1, 2], [1, 2])
# print is_cycle([2, 3, 4], [2, 3, 4])

# print cycle([1, 2, 3, 4, 2, 3, 4])
# print cycle([1, 2, 3, 4])
print(cycle([1, 2, 1, 2, 3, 4]))
