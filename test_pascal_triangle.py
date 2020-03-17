from unittest import TestCase

from CombPermCount import comb_count
from PascalTriangle import pascal_recur, pascal_iter

class TestPascalTriangle(TestCase):
    def test_pascal_recur(self):
        for n in range(50):
            for k in range(n + 1):
                print(n, k)
                self.assertEqual(comb_count(n, k), pascal_recur(n, k))

    def test_pascal_iter(self):
        for n in range(50):
            for k in range(n + 1):
                print(n, k)
                self.assertEqual(comb_count(n, k), pascal_iter(n, k))
