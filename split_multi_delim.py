# split the string with the specified delimiters
# output list should include the delimiter
# function allows multiple delimiters
import unittest
import re


def split_multi_delim(s, delim, **kwargs):
    if s is None or s == '':
        return []
    if kwargs.get('nodelim'):
        return re.split('[' + delim + ']', s)
    else:
        return re.split('([' + delim + '])', s)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        self.assertEqual(split_multi_delim('qwer/asdf/zxcv', '/'), ['qwer', '/', 'asdf', '/', 'zxcv'])
        self.assertEqual(split_multi_delim('qwer/asdf/zxcv', '/', nodelim=False), ['qwer', '/', 'asdf', '/', 'zxcv'])
        self.assertEqual(split_multi_delim('qwer/asdf/zxcv', '/', nodelim=True), ['qwer', 'asdf', 'zxcv'])
        self.assertEqual(split_multi_delim('qwer/asdf#zxcv', '/#'), ['qwer', '/', 'asdf', '#', 'zxcv'])
        self.assertEqual(split_multi_delim('qwer/asdf#zxcv', '/#', nodelim=False), ['qwer', '/', 'asdf', '#', 'zxcv'])
        self.assertEqual(split_multi_delim('qwer/asdf#zxcv', '/#', nodelim=True), ['qwer', 'asdf', 'zxcv'])
        self.assertEqual(split_multi_delim(None, '/'), [])
        self.assertEqual(split_multi_delim('', '/'), [])
        self.assertEqual(split_multi_delim('a', '/'), ['a'])
        self.assertEqual(split_multi_delim('a', '/', nodelim=False), ['a'])
        self.assertEqual(split_multi_delim('a', '/', nodelim=True), ['a'])
        self.assertEqual(split_multi_delim('ab', '/'), ['ab'])
        self.assertEqual(split_multi_delim('ab', '/', nodelim=False), ['ab'])
        self.assertEqual(split_multi_delim('ab', '/', nodelim=True), ['ab'])


if __name__ == '__main__':
    unittest.main()

# print split_multi_delim('qwer/asdf/zxcv', '/', nodelim=True)
# print split_multi_delim('qwer/asdf/zxcv', '/', nodelim=False)
# print split_multi_delim('qwer/asdf/zxcv', '/')
# print split_multi_delim(None, '/')
# print split_multi_delim('', '/')
# print 'asdf/qwer'.split('/')
