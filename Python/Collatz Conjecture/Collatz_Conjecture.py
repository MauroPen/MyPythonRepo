# Collatz Conjecture

from numpy import sort, array, append, where
from pandas import DataFrame, Series, ExcelWriter, merge
from IPython.display import display
from matplotlib import pyplot, gridspec
from datetime import datetime
from os import getcwd

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

def normalizeValues(Table, Range, Max_Iterations):

    print("\n\nPreparing data for plotting! Please Wait...\n")

    for i in range(1, (Range[1] - Range[0] + 2), 1): #Need to add as many "0" as necessary to make every array having as many values as the longest iteration

        print(" {Status}%" .format(Status = int((i / (Range[1] - Range[0] + 1)) * 100)), end = "\r")
        
        while (len(Table.at[i, "Obtained Values"]) != Max_Iterations + 1):

            Table.at[i, "Obtained Values"] = append(Table.at[i, "Obtained Values"], int(0))

    return Table

def transformArraysIntoColumns(Table, Range, Max_Iterations):

    Transform_Array_Into_DataFrame = DataFrame(data = Table["Obtained Values"].values.tolist(), dtype = int, index = list(range(1, (Range[1] - Range[0] + 2), 1)), columns = ColumnLabelsArray(Max_Iterations))

    Table = merge(Table.drop(columns = ["Starting Number", "Obtained Values"]), Transform_Array_Into_DataFrame, how = "inner", left_index = True, right_index = True)
    
    return Table

def ColumnLabelsArray(Max_Iterations): 

    ColumnLabels = array("Starting Number")

    for j in range(1, Max_Iterations + 1, 1):
        
        ColumnLabels = append(ColumnLabels, "Iteration " + str(j))
        
    return ColumnLabels

#Setting Default Values

running = bool(True)

Default_Range = array([10, 100])

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

    Execution_Table = DataFrame({"Starting Number": list(range(Range[0], Range[1] + 1, 1))}, index = list(range(1, (Range[1] - Range[0] + 2), 1))) #Creating the table collecting valuesobtained for each starting number

    Execution_Table["Obtained Values"] = Series(dtype = object) #Creating an empty column hosting the obtained values in array form

    Execution_Table["Obtained Values"] = Execution_Table["Obtained Values"].apply(lambda column : [])

    Max_Number_Tag = {
        "Id": 1,
        "Starting Number": Range[0],
        "Max Number": Range[1],
        "Iteration": 0
    }

    Max_Iterations_Tag = {
        "Id": 1,
        "Starting Number": Range[0],
        "Max Iterations": 0
    }

    print("\n\nProcessing! Please Wait...\n")

    for i in range(1, (Range[1] - Range[0] + 2), 1):

        #print("Current Iteration: {Iteration} / {Total_Iterations}" .format(Iteration = i, Total_Iterations = (Range[1] - Range[0] + 1)), end = "\r")

        print(" {Status}%" .format(Status = int((i / (Range[1] - Range[0] + 1)) * 100)), end = "\r")

        Iteration_Array = array([Range[0] + i - 1])

        while(Iteration_Array[-1] != 1):

            if (Iteration_Array[-1] % 2 == 0):

                Iteration_Array = append(Iteration_Array, Iteration_Array[-1] / 2)

            else:

                Iteration_Array = append(Iteration_Array, Iteration_Array[-1] * 3 + 1)

        if (Max_Number_Tag["Max Number"] < max(Iteration_Array)):

            Max_Number_Tag["Id"] = i
            Max_Number_Tag["Starting Number"] = (Range[0] + i - 1)
            Max_Number_Tag["Max Number"] = int(max(Iteration_Array))
            Max_Number_Tag["Iteration"] = where(Iteration_Array == max(Iteration_Array))[0][0]

        if (Max_Iterations_Tag["Max Iterations"] < len(Iteration_Array)):

            Max_Iterations_Tag["Id"] = i
            Max_Iterations_Tag["Starting Number"] = (Range[0] + i - 1)
            Max_Iterations_Tag["Max Iterations"] = len(Iteration_Array)

        Execution_Table.at[i, "Obtained Values"] = Iteration_Array.astype(int)

    Execution_Table = normalizeValues(Execution_Table, Range, Max_Iterations_Tag["Max Iterations"]) #Necessary to allow plotting values all together (same-length arrays)

    # Graph

    Iterations_Axis = list(range(0, Max_Iterations_Tag["Max Iterations"] + 1, 1))

    gs = gridspec.GridSpec(3, 1)
    fig = pyplot.figure()

    ax1 = fig.add_subplot(gs[0, 0])
    pyplot.setp(ax1.get_xticklabels(), visible = False) #Hiding ticks for readability
    ax1.set_title("Results Overview")
    ax1.set_ylim([1, Max_Number_Tag["Max Number"] * 1.05])
    ax1.set_ylabel("Number")
    pyplot.grid()

    ax2 = fig.add_subplot(gs[1, 0], sharex = ax1)
    pyplot.setp(ax2.get_xticklabels(), visible = False) #Hiding ticks for readability
    ax2.set_title("Longest Iteration")
    ax2.set_ylim([1, Max_Number_Tag["Max Number"] * 1.05])
    ax2.set_ylabel("Number")
    pyplot.grid()

    ax3 = fig.add_subplot(gs[2, 0], sharex = ax1)
    ax3.set_title("Highest Number")
    ax3.set_xlabel("Iteration")
    ax3.set_ylim([1, Max_Number_Tag["Max Number"] * 1.05])
    ax3.set_ylabel("Number")
    pyplot.grid()

    # LEGACY (TO BE DELETED)

    print("\n\nGenerating the graphs! Please Wait...\n")

    for i in range(1, (Range[1] - Range[0] + 2), 1):

        print(" {Status}%" .format(Status = int((i / (Range[1] - Range[0] + 1)) * 100)), end = "\r")
        
        ax1.plot(Iterations_Axis, Execution_Table.at[i, "Obtained Values"], linestyle = ":")
    
    ax2.plot(Iterations_Axis, Execution_Table.at[Max_Iterations_Tag["Id"], "Obtained Values"], linewidth = 2, color = "k", label = "Longest Iteration")

    ax3.plot(Iterations_Axis, Execution_Table.at[Max_Number_Tag["Id"], "Obtained Values"], linewidth = 2, color = "b", label = "Highest Number")

    # Data insights
    
    print("\nThe starting number {Starting_Number} has triggered the highest number of iterations: {Iterations}\n" .format(Starting_Number = Max_Iterations_Tag["Starting Number"], Iterations = Max_Iterations_Tag["Max Iterations"]))

    print("\n\nThe starting number {Starting_Number} has generated the highest number ({Max_Number}) during its iteration number {Iteration}\n" .format(Starting_Number = Max_Number_Tag["Starting Number"], Max_Number = Max_Number_Tag["Max Number"], Iteration = Max_Number_Tag["Iteration"]))
    
    pyplot.show()
    
    # Export data

    print("\nWould you like to export the data obtained during the computation in an Excel file? (y/n)\n\nWARNING! The new file would be created in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = getcwd()))

    if (yn_input_check() == True):

        Execution_Table = transformArraysIntoColumns(Execution_Table, Range, Max_Iterations_Tag["Max Iterations"])

        Datetime_String = datetime.now().strftime("%d_%m_%Y - %H_%M_%S")

        with ExcelWriter ("Collatz Conjecture Results ({Timestamp}).xlsx" .format(Timestamp = Datetime_String)) as writer:

            Execution_Table.to_excel(writer, sheet_name = "Execution Table", index = True)

            print("\n\nIn this directory: \"{Current_Working_Directory}\" a file named \"Collatz Conjecture Results ({Timestamp}).xlsx\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), Timestamp = Datetime_String))
    
    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()