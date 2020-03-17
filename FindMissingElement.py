import unittest
from random import randrange, shuffle


def find_missing(arr1, arr2):
    missing_num = 0
    for n in arr1 + arr2:
        missing_num ^= n
    return missing_num


def create_random_array(arr_size, int_range):
    return [randrange(int_range) for i in range(arr_size)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(find_missing([5, 4, 3, 2, 1], [5, 4, 2, 1]), 3)

        for i in range(100):
            a1 = create_random_array(randrange(1, 25), randrange(1, 100))
            a2 = list(a1)
            shuffle(a2)
            missing_num = a2[0]
            a2.pop(0)
            # print a1, a2, missing_num
            self.assertEqual(find_missing(a1,a2), missing_num)


if __name__ == '__main__':
    unittest.main()

# print find_missing([5, 4, 3, 2, 1], [5, 4, 2, 1])
