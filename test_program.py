# test_program.py
import unittest
from io import StringIO
from unittest.mock import patch

import program  # This is the file containing the greet function


class TestProgram(unittest.TestCase):

    @patch('builtins.input', side_effect=['Alice'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_greet(self, mock_stdout, mock_input):
        program.greet()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, Alice!")


if __name__ == '__main__':
    unittest.main()
