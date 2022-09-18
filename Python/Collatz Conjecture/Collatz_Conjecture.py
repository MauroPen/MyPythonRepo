# Collatz Conjecture

from numpy import sort

def yn_input_check():

    char_input = "Default"

    while(not(char_input == "y" or char_input == "n")):

        char_input = input()

        if char_input == "y":

            return True

        elif char_input == "n":

            return False

        else:

            print("\nThe inserted value is not valid, please input y or n\n")

def int_input_check():

    int_input = -1

    while (int_input < 0):

        try:
            
            int_input = int(input())
    
            while(int_input < 0):

                print("\nThe inserted value is not valid, please input a number higher than 0:\n")

                int_input = int(input())

            return int_input
        
        except:

            print("\nThe inserted value is not valid, please input a number higher than 0:\n")

            int_input = -1

#Setting Default Values

running = bool(True)

Default_Range = [1, 50]

while (running == True):

    print("\n\nWelcome to the Collatz Conjecture program!\n\nDo you want to run it in Default Mode? (y/n)\n")

    # Variables settings

    Range = [1, 0] #Initialized to unsatisfy the condition in "else" 

    Default_mode = yn_input_check()

    if (Default_mode == True):

        Range = Default_Range

    else:

        while (Range[0] > Range[1]):

            print("\nPlease input the number that you would like to start the computation from:\n")
            
            Range[0] = int_input_check()

            print("\nAmazing! Now, please input the last number of the computation:\n")
            
            Range[1] = int_input_check()

            if (Range[0] > Range[1]):

                print("\nThe last number inputed is lower than the first one. Would you like to revert their order and continue with the execution? (y/n)\n\n(Otherwise, you will be required to input the two values again)\n")

                if (yn_input_check() == True):

                    Range = sort(Range)

    print("\n", Range, "\n")

    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()