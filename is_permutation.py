from random import randrange, shuffle
from collections import Counter
import unittest


def is_permutation(a1, a2):
    if len(a1) != len(a2):
        return False
    counter = Counter(a1)
    for e in a2:
        counter[e] -= 1
        if counter[e] < 0:
            return False
    return True


def create_random_array(n, r):
    return [randrange(r) for i in range(n)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_permutation([], []), True)
        self.assertEqual(is_permutation([1], []), False)
        self.assertEqual(is_permutation([1, 2], []), False)
        self.assertEqual(is_permutation([1, 2, 3], []), False)
        self.assertEqual(is_permutation([], [1]), False)
        self.assertEqual(is_permutation([], [1, 2]), False)
        self.assertEqual(is_permutation([], [1, 2, 3]), False)
        self.assertEqual(is_permutation([1], [1]), True)
        self.assertEqual(is_permutation([1, 2], [1, 2]), True)
        self.assertEqual(is_permutation([1, 2], [2, 1]), True)
        self.assertEqual(is_permutation([2, 1], [1, 2]), True)
        self.assertEqual(is_permutation([1, 2], [1, 2, 3]), False)
        self.assertEqual(is_permutation([1, 2, 3], [1, 2]), False)

        for i in range(100):
            a1 = create_random_array(3, 3)
            a2 = create_random_array(3, 3)
            # print a1, a2, sorted(a1) == sorted(a2)
            self.assertEqual(is_permutation(a1, a2), sorted(a1) == sorted(a2))

        for i in range(100):
            a1 = create_random_array(10, 100)
            a2 = list(a1)
            shuffle(a2)
            # print a1, a2, sorted(a1) == sorted(a2)
            self.assertEqual(is_permutation(a1, a2), sorted(a1) == sorted(a2))


if __name__ == '__main__':
    unittest.main()

# arr1 = []
# arr2 = []
# print is_permutation(arr1, arr2)
