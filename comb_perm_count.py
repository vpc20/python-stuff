from itertools import combinations, permutations
from math import factorial


# can be used to get binomial coefficient
#    n!
# ---------
# r! (n-r)!

def comb_count(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


#    n!
# --------
#  (n-r)!

def perm_count(n, r):
    return int(factorial(n) / factorial(n - r))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    print('------------permutations-----------------')
    for i in range(1, len(arr) + 1):
        # print([comb for comb in combinations(arr, i)])
        print(len([perm for perm in permutations(arr, i)]))

    print('-' * 64)

    for i in range(1, len(arr) + 1):
        print(perm_count(len(arr), i))

    print('------------combinations-----------------')
    for i in range(1, len(arr) + 1):
        # print([comb for comb in combinations(arr, i)])
        print(len([comb for comb in combinations(arr, i)]))

    print('-' * 64)

    for i in range(1, len(arr) + 1):
        print(comb_count(len(arr), i))

    print(comb_count(5, 3))
