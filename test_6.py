import unittest
from 6 import function

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(function(11), 2640)