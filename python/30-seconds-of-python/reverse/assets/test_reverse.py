import unittest
from reverse import *


class TestReverse(unittest.TestCase):
    
    def test_reverse(self):
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse((4, 5, 6)), (6, 5, 4))
        self.assertEqual(reverse([]), [])