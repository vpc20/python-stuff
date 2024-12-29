import unittest
from random import randrange, choice


def partition(arr, start, end):
    pivot = arr[start]
    part_idx = start
    for i in range(start, end + 1):
        if arr[i] < pivot:
            part_idx += 1
            arr[i], arr[part_idx] = arr[part_idx], arr[i]
    arr[start], arr[part_idx] = arr[part_idx], arr[start]
    return part_idx


def kth_smallest(arr, k):
    if k > len(arr):
        return None
    return kth_smallest_aux(arr, k, 0, len(arr) - 1)


def kth_smallest_aux(arr, k, start, end):
    if start > end:
        return None
    part_idx = partition(arr, start, end)

    if k - 1 == part_idx:
        return arr[part_idx]
    elif k - 1 < part_idx:
        return kth_smallest_aux(arr, k, start, part_idx - 1)
    else:
        return kth_smallest_aux(arr, k, part_idx + 1, end)


def random_int_array(max_arr_size, max_int):
    return [randrange(1, max_int + 1) for i in range(randrange(1, max_arr_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        for _ in range(10000):
            a = random_int_array(20, 1000)
            if len(a) > 0:
                k = randrange(len(a))
                if k == 0:
                    k = 1
                print(a, k)
                self.assertEqual(kth_smallest(a, k), sorted(a)[k - 1])


if __name__ == '__main__':
    unittest.main()

    # print kth_smallest([5], 1)
    # print kth_smallest([2, 5], 1)
    # print kth_smallest([2, 5], 2)
    # print kth_smallest([5, 2], 1)
    # print kth_smallest([5, 2], 2)
    # print kth_smallest([100, 99, 98], 1)
    # print kth_smallest([100, 99, 98], 2)
    # print kth_smallest([100, 99, 98], 3)

    # print kth_smallest([18, 35, 462], 2)
    # [18, 35, 462] 2
