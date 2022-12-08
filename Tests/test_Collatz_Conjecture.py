from unittest import TestCase, main
from numpy import array
from datetime import date

from Scripts.Collatz_Conjecture.Dependency import normalizeArray, ColumnLabelsArray       #Valid only when testing scripts with absolute modules (no personal modules)

class TestNormalizeArray(TestCase):

    def test_normalize1(self):

        Array = array([[0, [array([0])]],
                       [1, [array([1, 0])]],
                       [2, [array([2, 1, 0])]],
                       [3, [array([3, 10, 5, 16, 8, 4, 2, 1, 0])]]], dtype = object)

        Range = [1, 3]

        Max_Iterations = 8

        expectedResult_Array = array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [1, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [2, 1, 0, 0, 0, 0, 0, 0, 0],
                                      [3, 10, 5, 16, 8, 4, 2, 1, 0]], dtype = object)

        result_Array = normalizeArray(Array, Range, Max_Iterations)

        self.assertTrue(((result_Array == expectedResult_Array).all()), "Test failed! The algorithm has not produced same-length arrays.")

class TestColumnLabelsArray(TestCase):

    def test_labels1(self):

        Max_Iterations = 3

        expectedResult_Labels = array(["Starting Number",
                                 "Iteration 1",
                                 "Iteration 2",
                                 "Iteration 3"])

        result_Labels = ColumnLabelsArray(Max_Iterations)

        self.assertTrue((result_Labels == expectedResult_Labels).all(), "Test failed! The function did not return the rigth column labels.")

if __name__ == '__main__':

    main()