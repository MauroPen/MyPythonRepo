from unittest import TestCase, main
from numpy import array, full

from Scripts.Reproduction_Simulator.Dependency import compute_mean       #Valid only when testing scripts with absolute modules (no personal modules)

class TestComputeMean(TestCase):

    def test_computation1(self):

        Starting_N = 10

        Period = 2

        Repeat = 3

        N_Array = array([full(Period + 1, 0),       #First element is a dummy because iterations start from 1 
                        [10, 15, 20],
                        [10, 10, 8],
                        [10, 14, 5]])

        expectedAvg_Array = [10.0, 13.0, 11.0]

        Avg_Array = compute_mean(N_Array, Repeat, Period, Starting_N)

        self.assertTrue(((Avg_Array == expectedAvg_Array)), "Test failed! The algorithm has not produced the correct average values.")

if __name__ == '__main__':

    main()