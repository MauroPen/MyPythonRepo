import re
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from shared.Common import yn_input_check, int_input_check, get_ordinal
from Fibonacci_Series.Dependency import fibonacci, print_fibonacci_series

running = bool(True)

Default_Num = 50

while (running == True):

    print("\n\nWelcome to Fibonacci!\n")

    print("\nDo you want to compute the {Ordinal} Fibonacci number? (y/n)\n" .format(Ordinal = get_ordinal(Default_Num)))

    if (yn_input_check()):

        number = Default_Num

    else:

        print("\nPlease, input a number representing the index of the Fibonacci series that you want to know:\n")

        number = int_input_check()

    print("\nThe {Ordinal} term of the Fibonacci series is: {Fibonacci}\n".format(Ordinal = get_ordinal(number), Fibonacci = fibonacci(number)))

    print("\nWould you like to know how the Fibonacci series looks like until this number? (y/n)\n")

    if (yn_input_check()):

        print_fibonacci_series(number)

    print("\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()