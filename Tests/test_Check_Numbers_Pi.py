from unittest import TestCase, main

from Scripts.Check_Numbers_Pi.Dependency import main_computation, retrieve_pi

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

if __name__ == '__main__':

    main()