import unittest
from is_prime import *

from math import sqrt

def is_prime(n):
  if n <= 1 or (n % 2 == 0 and n > 2):
    return False
  return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(37))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(43))
        self.assertTrue(is_prime(47))
        self.assertTrue(is_prime(53))
        self.assertTrue(is_prime(59))
        self.assertTrue(is_prime(61))
        self.assertTrue(is_prime(67))
        self.assertTrue(is_prime(71))
        self.assertTrue(is_prime(73))
        self.assertTrue(is_prime(79))
        self.assertTrue(is_prime(83))
        self.assertTrue(is_prime(89))
        self.assertTrue(is_prime(97))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(21))
        self.assertFalse(is_prime(22))
        self.assertFalse(is_prime(24))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(26))
        self.assertFalse(is_prime(27))
        self.assertFalse(is_prime(28))
        self.assertFalse(is_prime(30))
        self.assertFalse(is_prime(32))
        self.assertFalse(is_prime(33))
        self.assertFalse(is_prime(34))
        self.assertFalse(is_prime(35))
        self.assertFalse(is_prime(36))
        self.assertFalse(is_prime(38))
        self.assertFalse(is_prime(39))
        self.assertFalse(is_prime(40))
        self.assertFalse(is_prime(42))
        self.assertFalse(is_prime(44))
        self.assertFalse(is_prime(45))
        self.assertFalse(is_prime(46))
        self.assertFalse(is_prime(48))
        self.assertFalse(is_prime(49))
        self.assertFalse(is_prime(50))
        self.assertFalse(is_prime(51))
        self.assertFalse(is_prime(52))
        self.assertFalse(is_prime(54))
        self.assertFalse(is_prime(55))
        self.assertFalse(is_prime(56))
        self.assertFalse(is_prime(57))
        self.assertFalse(is_prime(58))
        self.assertFalse(is_prime(60))
        self.assertFalse(is_prime(62))
        self.assertFalse(is_prime(63))
        self.assertFalse(is_prime(64))
        self.assertFalse(is_prime(65))
        self.assertFalse(is_prime(66))
        self.assertFalse(is_prime(68))
        self.assertFalse(is_prime(69))
        self.assertFalse(is_prime(70))
        self.assertFalse(is_prime(72))
        self.assertFalse(is_prime(74))
        self.assertFalse(is_prime(75))
        self.assertFalse(is_prime(76))
        self.assertFalse(is_prime(77))
        self.assertFalse(is_prime(78))
        self.assertFalse(is_prime(80))
        self.assertFalse(is_prime(81))
        self.assertFalse(is_prime(82))
        self.assertFalse(is_prime(84))
        self.assertFalse(is_prime(85))
        self.assertFalse(is_prime(86))
        self.assertFalse(is_prime(87))
        self.assertFalse(is_prime(88))
        self.assertFalse(is_prime(90))
        self.assertFalse(is_prime(91))
        self.assertFalse(is_prime(92))
        self.assertFalse(is_prime(93))
        self.assertFalse(is_prime(94))
        self.assertFalse(is_prime(95))
        self.assertFalse(is_prime(96))
        self.assertFalse(is_prime(98))
        self.assertFalse(is_prime(99))

if __name__ == '__main__':
    unittest.main()