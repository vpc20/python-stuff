from unittest import TestCase
from NestedListDepth import list_depth_iter, list_depth_recur


class TestListDepth(TestCase):
    def test_list_depth(self):
        arr = [1]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [2]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [1, 2, 3]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [1, [2]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[1, 2], 3]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [1, [2, 3]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [1, [2, 3, [4]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[8, 9], 1, [2, 3, [4]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[[[[1]]]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [1, [2, 2], 1, [2, 2], 1, [2, 2]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[8, 9], 1, [[1], 2, 3]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[1, 2], [3, 4]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[1, 2], [3, 4, [1]], [5, 6]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[1], 2]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [1, [2], [3, [4]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[3, [4]], 1, [2]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[3, [4], 1, [2]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[2]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[[3]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[[[4]]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[8, 9], 1, [2, 3, [4]]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))
        arr = [[8, [1]], [7], [6]]
        self.assertEqual(list_depth_iter(arr), list_depth_recur(arr))

