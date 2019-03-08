import unittest
from function import fcn

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fcn(10), 23)

