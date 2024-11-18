import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest import TestCase, main

from Check_Numbers_Pi.dependency import main_computation, check_occurrencies, retrieve_pi

class TestMainComputation(TestCase):

    def test_computation_ok(self):

        testInput = "510"

        expectedResult = {
            "Digits Checked": 48,
            "Pi Until": "314159265358979323846264338327950288419716939937510",
            "Not Found": False
        }

        result = main_computation(testInput)

        self.assertTrue(expectedResult == result, "Test failed! Wrong results have been obtained.")

    def test_computation_not_found(self):

        testInput = "06041997"

        expectedResult = {
            "Digits Checked": 1000001,
            "Pi Until": retrieve_pi(),
            "Not Found": True
        }

        result = main_computation(testInput)

        self.assertTrue(expectedResult == result, "Test failed! Wrong results have been obtained.")

class TestCheckOccurrencies(TestCase):

    def test_check_occurrencies(self):

        testInput = "6497"

        expectedResult = 83

        result = check_occurrencies(testInput, main_computation(testInput)["Digits Checked"])

        self.assertTrue(expectedResult == result, "Test failed! Wrong results have been obtained.")

    def test_check_single_occurrency(self):

        testInput = "666666"

        expectedResult = 1

        result = check_occurrencies(testInput, main_computation(testInput)["Digits Checked"])

        self.assertTrue(expectedResult == result, "Test failed! Wrong results have been obtained.")

if __name__ == '__main__':

    main()