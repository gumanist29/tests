import unittest
from 10 import sum_Prime
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Prime(10), 17)

#     def test_prime(self):
#     for i in range(2, 11):
#         with self.subTest(i=i):
#             self.assertEqual(11%i, !0)