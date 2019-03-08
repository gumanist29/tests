import unittest
from 5 import lcm
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(lcm(13195), 29)