import unittest


# assume n is always a positive integer
# def create_nested_list(n):
#     nested_list = []
#     if n == 1:
#         return []
#     nested_list.append(create_nested_list(n - 1))
#     return nested_list


def create_nested_list(n):
    nested_list = []
    for i in range(n - 1):
        nested_list = [nested_list]
    return nested_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        self.assertEqual(create_nested_list(1), [])
        self.assertEqual(create_nested_list(2), [[]])
        self.assertEqual(create_nested_list(3), [[[]]])
        self.assertEqual(create_nested_list(4), [[[[]]]])
        self.assertEqual(create_nested_list(5), [[[[[]]]]])


if __name__ == '__main__':
    unittest.main()

# print(create_nested_list(1))
# print(create_nested_list(5))
