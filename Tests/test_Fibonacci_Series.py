import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest import TestCase, main

from Fibonacci_Series.dependency import fibonacci

class TestMainComputation(TestCase):

    def test_fibonacci_0(self):

        expectedResult = 0

        result = fibonacci(0)

        self.assertTrue(expectedResult == result, "Test failed! Wrong results have been obtained.")

    def test_fibonacci_1(self):

        expectedResult = 1

        result = fibonacci(1)

        self.assertTrue(expectedResult == result, "Test failed! Wrong results have been obtained.")

    def test_fibonacci_any(self):

        expectedResult = 13

        result = fibonacci(8)

        self.assertTrue(expectedResult == result, "Test failed! Wrong results have been obtained.")

if __name__ == '__main__':

    main()