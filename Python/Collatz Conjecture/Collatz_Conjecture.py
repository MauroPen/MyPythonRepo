# Collatz Conjecture

from numpy import sort, array, append
from pandas import DataFrame, Series
from IPython.display import display

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

Default_Range = array([10, 15])

while (running == True):

    print("\n\nWelcome to the Collatz Conjecture program!\n\nDo you want to run it in Default Mode? (y/n)\n")

    # Variables settings

    Range = [1, 0] #Initialized to unsatisfy the condition in "else" 

    Default_Mode = yn_input_check()

    if (Default_Mode == True):

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

    # Computation

    Execution_Table = DataFrame({"Starting Numbers": list(range(Range[0], Range[1] + 1, 1))}, index = list(range(1, (Range[1] - Range[0] + 2), 1))) #Creating the table collecting valuesobtained for each starting number

    Execution_Table["Obtained Values"] = Series(dtype = object) #Creating an empty column hosting the obtained values in array form

    Execution_Table["Obtained Values"] = Execution_Table["Obtained Values"].apply(lambda column: [])

    Max_Number = Range[1]

    Max_Iterations = 0

    for i in range(1, (Range[1] - Range[0] + 2), 1):

        Iteration_Array = array([Range[0] + i - 1])

        while(Iteration_Array[-1] != 1):

            if (Iteration_Array[-1] % 2 == 0):

                Iteration_Array = append(Iteration_Array, Iteration_Array[-1] / 2)

            else:

                Iteration_Array = append(Iteration_Array, Iteration_Array[-1] * 3 + 1)

        if (Max_Number < max(Iteration_Array)):

            Max_Number = max(Iteration_Array)

        if (Max_Iterations < (len(Iteration_Array) - 1)):

            Max_Iterations = (len(Iteration_Array) - 1)

        Execution_Table.at[i, "Obtained Values"] = Iteration_Array.astype(int)

    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()