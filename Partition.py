import unittest
from random import randrange


def is_low_high_partition(arr, part_idx):
    pivot = arr[part_idx]
    for i in range(part_idx):
        if arr[i] > pivot:
            return False
    for i in range(part_idx + 1, len(arr)):
        if arr[i] < pivot:
            return False
    return True


def partition(arr, start, end):
    pivot = arr[start]
    part_idx = start
    for i in range(start, end + 1):
        if arr[i] < pivot:
            part_idx += 1
            arr[i], arr[part_idx] = arr[part_idx], arr[i]
    arr[start], arr[part_idx] = arr[part_idx], arr[start]
    return part_idx


def random_int_array(max_arr_size, max_int):
    return [randrange(max_int + 1) for i in range(randrange(max_arr_size + 1))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        for i in range(10000):
            a1 = random_int_array(20, 1000)
            if a1:
                print(a1)
                part_idx = partition(a1, 0, len(a1) - 1)
                print(part_idx, a1)
                self.assertEqual(is_low_high_partition(a1, part_idx), True)


if __name__ == '__main__':
    unittest.main()

# a = [5,2]
# print partition(a,0,1)
# print a
