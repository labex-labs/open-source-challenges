import sys
import unittest
from io import StringIO

sys.path.append("/home/labex/project")
from use_of_filter import use_of_filter

class Test(unittest.TestCase):

    def test_use_of_filter(self):
        li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n"
        with StringIO() as buffer:
            sys.stdout = buffer
            use_of_filter()
            sys.stdout = sys.__stdout__
            self.assertEqual(buffer.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
