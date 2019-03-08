import unittest
from 2 import fib

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fib(14), 24)