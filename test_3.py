import unittest
from 3 import LargestPrimeFactor

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(LargestPrimeFactor(13195), 29)