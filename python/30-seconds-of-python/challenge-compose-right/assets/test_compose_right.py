import unittest
import sys

sys.path.append("/home/labex/project")
from compose_right import *

from functools import reduce


def compose_right(*fns):
    return reduce(lambda f, g: lambda *args: g(f(*args)), fns)


class TestComposeRight(unittest.TestCase):
    def test_compose_right(self):
        add_one = lambda x: x + 1
        multiply_by_two = lambda x: x * 2
        subtract_three = lambda x: x - 3

        composed = compose_right(add_one, multiply_by_two, subtract_three)
        self.assertEqual(composed(5), 7)
        self.assertEqual(composed(10), 17)
        self.assertEqual(composed(0), -3)
