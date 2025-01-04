# test_program.py

import unittest
from io import StringIO
from unittest.mock import patch

import main  # Replace with the name of the module containing the main function


class TestShell(unittest.TestCase):

    @patch('builtins.input', side_effect=['echo Hello', 'type echo', 'pwd', 'xxx', 'exit 0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        main.main()
        self.assertEqual(mock_stdout.getvalue(),
                         '$ Hello\n$ echo is a shell builtin\n$ C:\\Users\\vpc\\PycharmProjects\\codecrafters-shell-python\\app\n$ xxx: command not found\n$ ')


if __name__ == '__main__':
    unittest.main()
