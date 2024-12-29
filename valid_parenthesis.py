import unittest


# def valid_brackets(s):
#     open_brackets = ['(', '[', '{']
#     close_brackets = {')': '(', ']': '[', '}': '{'}
#     stack = []
#     for ch in s:
#         if ch in open_brackets:
#             stack.append(ch)
#         elif ch in close_brackets:
#             if stack and stack[-1] == close_brackets[ch]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0     # return not bool(stack)

def valid_brackets(s):
    open_brackets = ['(', '[', '{']
    close_brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in open_brackets:
            stack.append(ch)
        elif ch in close_brackets:
            if not stack or stack.pop() != close_brackets[ch]:
                return False
    return len(stack) == 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(valid_brackets(''), True)

        self.assertEqual(valid_brackets('()'), True)
        self.assertEqual(valid_brackets('(())'), True)
        self.assertEqual(valid_brackets('((()))'), True)
        self.assertEqual(valid_brackets('()()'), True)
        self.assertEqual(valid_brackets('()()()'), True)

        self.assertEqual(valid_brackets('[]'), True)
        self.assertEqual(valid_brackets('[[]]'), True)
        self.assertEqual(valid_brackets('[[[]]]'), True)
        self.assertEqual(valid_brackets('[][]'), True)
        self.assertEqual(valid_brackets('[][][]'), True)

        self.assertEqual(valid_brackets('{}'), True)
        self.assertEqual(valid_brackets('{{}}'), True)
        self.assertEqual(valid_brackets('{{{}}}'), True)
        self.assertEqual(valid_brackets('{}{}'), True)
        self.assertEqual(valid_brackets('{}{}{}'), True)

        self.assertEqual(valid_brackets('()[]{}'), True)
        self.assertEqual(valid_brackets('([]){()[]{}}'), True)

        self.assertEqual(valid_brackets('('), False)
        self.assertEqual(valid_brackets(')'), False)
        self.assertEqual(valid_brackets(')('), False)
        self.assertEqual(valid_brackets('))(('), False)
        self.assertEqual(valid_brackets(')))((('), False)

        self.assertEqual(valid_brackets('['), False)
        self.assertEqual(valid_brackets(']'), False)
        self.assertEqual(valid_brackets(']['), False)
        self.assertEqual(valid_brackets(']][['), False)
        self.assertEqual(valid_brackets(']]][[['), False)

        self.assertEqual(valid_brackets('{'), False)
        self.assertEqual(valid_brackets('}'), False)
        self.assertEqual(valid_brackets('}{'), False)
        self.assertEqual(valid_brackets('}}{{'), False)
        self.assertEqual(valid_brackets('}}}{{{'), False)

        self.assertEqual(valid_brackets('({)'), False)
        self.assertEqual(valid_brackets('(])'), False)
        self.assertEqual(valid_brackets('({}[]})'), False)


if __name__ == '__main__':
    unittest.main()
