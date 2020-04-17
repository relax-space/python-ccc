import unittest
import test


class TestFunc(unittest.TestCase):
    def test_average(self):
        self.assertEqual(test.average([20, 30, 70]), 40.0)
        self.assertEqual(round(test.average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, test.average, [])
        self.assertRaises(TypeError, test.average, 20, 30, 70)

unittest.main()