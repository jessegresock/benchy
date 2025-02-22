import unittest
from benchy import functions


class TestFunctions(unittest.TestCase):

    def test_positive_timer(self):
        """Test measure_time returns only a positive timing value"""
        result, time = functions.measure_time(print, 'Hello, World!')
        self.assertEqual(time > 0)

    def test_tuple_return(self):
        """Test measure_time return type is of type tuple"""
        ttuple = functions.measure_time(print, "Hello, World!")
        self.assertIsInstance(ttuple, tuple)


if __name__ == '__main__':
    unittest.main()