from benchy.decorators import timer

import contextlib
import io
import unittest


class TestDecorators(unittest.TestCase):

    def test_timer_decorator(self):
        @timer
        def multiply(a, b):
            return a * b
        
        capture_output = io.StringIO()
        with contextlib.redirect_stdout(capture_output):
            multiply(2, 2)

        output = capture_output.getvalue()
        self.assertIn(f"Function {multiply.__name__} executed in", output)


if __name__ == '__main__':
    unittest.main()