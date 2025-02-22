import unittest
from benchy import functions


class TestFunctions(unittest.TestCase):

    def multiply(self, a, b):
        return a * b

    def test_positive_timer(self):
        """Test measure_time returns only a positive timing value"""
        result, time = functions.measure_time(self.multiply, 1, 2)
        self.assertTrue(time > 0)

    def test_tuple_return(self):
        """Test measure_time return type is of type tuple"""
        ttuple = functions.measure_time(self.multiply, 1, 2)
        self.assertIsInstance(ttuple, tuple)


if __name__ == '__main__':
    unittest.main()