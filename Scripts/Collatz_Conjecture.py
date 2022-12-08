from numpy import sort, array, append, concatenate, where
from pandas import DataFrame
from IPython.display import display
from matplotlib import pyplot, gridspec
from datetime import datetime
from tabulate import tabulate
from os import getcwd

from Common import yn_input_check, int_input_check, DataframeExport, export_dataframes

import Collatz_Conjecture.Dependency as CC

#Setting Default Values

running = bool(True)

Default_Range = array([10, 200])

while (running == True):

    print("\n\nWelcome to the Collatz Conjecture program!\n\nDo you want to run it in Default Mode? (y/n)\n")

    # Variables settings

    Range = [1, 0]      #Initialized to unsatisfy the condition in "else" 

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

    computationStartTime = datetime.now()

    Execution_Array = array([[0, [0]]], dtype = object)       #Initialized with meaningless values that will be ignored

    Max_Number_Tag = {
        "Id": 1,
        "Starting Number": Range[0],
        "Max Number": Range[0],
        "Iteration": 0
    }

    Max_Iterations_Tag = {
        "Id": 1,
        "Starting Number": Range[0],
        "Max Iterations": 0,
        "Max Number": Range[0],
        "Iteration": 0
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
            Max_Iterations_Tag["Max Number"] = int(max(Iteration_Array))
            Max_Iterations_Tag["Iteration"] = where(Iteration_Array == max(Iteration_Array))[0][0]

        Execution_Array = concatenate((Execution_Array, array([[i, [Iteration_Array.astype(int)]]], dtype = object)))

    Execution_Array = CC.normalizeArray(Execution_Array, Range, Max_Iterations_Tag["Max Iterations"])   #Necessary to allow plotting values all together (same-length arrays)
    
    computationEndTime = datetime.now()

    # Graph

    representationStartTime = datetime.now()

    Iterations_Axis = list(range(0, Max_Iterations_Tag["Max Iterations"] + 1, 1))

    gs = gridspec.GridSpec(3, 1)
    fig = pyplot.figure()

    ax1 = fig.add_subplot(gs[0, 0])
    pyplot.setp(ax1.get_xticklabels(), visible = False)     #Hiding ticks for readability
    ax1.set_title("Results Overview")
    ax1.set_ylim([1, Max_Number_Tag["Max Number"] * 1.05])
    ax1.set_ylabel("Number")
    pyplot.grid()

    ax2 = fig.add_subplot(gs[1, 0], sharex = ax1)
    pyplot.setp(ax2.get_xticklabels(), visible = False)     #Hiding ticks for readability
    ax2.set_title("Highest Number of Iterations: {Iterations} (Starting Number: {Starting_Number})" .format(Iterations = Max_Iterations_Tag["Max Iterations"], Starting_Number = Max_Iterations_Tag["Starting Number"]))
    ax2.set_ylim([1, Max_Iterations_Tag["Max Number"] * 1.05])
    ax2.set_ylabel("Number")
    pyplot.grid()

    ax3 = fig.add_subplot(gs[2, 0], sharex = ax1)
    ax3.set_title("Highest Number Obtained: {Max_Number} (Starting Number: {Starting_Number})" .format(Max_Number = Max_Number_Tag["Max Number"], Starting_Number = Max_Number_Tag["Starting Number"]))
    ax3.set_xlabel("Iteration #")
    ax3.set_ylim([1, Max_Number_Tag["Max Number"] * 1.05])
    ax3.set_ylabel("Number")
    pyplot.grid()

    print("\n\nGenerating the graphs! Please Wait...\n")

    for i in range(1, (Range[1] - Range[0] + 2), 1):

        print(" {Status}%" .format(Status = int((i / (Range[1] - Range[0] + 1)) * 100)), end = "\r")
        
        ax1.plot(Iterations_Axis, Execution_Array[i], linestyle = ":")
    
    ax2.plot(Iterations_Axis, Execution_Array[Max_Iterations_Tag["Id"]], linewidth = 2, color = "k", label = "Highest #Iterations")

    ax3.plot(Iterations_Axis, Execution_Array[Max_Number_Tag["Id"]], linewidth = 2, color = "b", label = "Highest Number")

    representationEndTIme = datetime.now()

    # Data insights

    totalExecutionTime = (computationEndTime - computationStartTime)

    totalRepresentationTime = (representationEndTIme - representationStartTime)
    
    print("\n\nThe starting number {Starting_Number} has triggered the highest number of iterations: {Iterations}\n" .format(Starting_Number = Max_Iterations_Tag["Starting Number"], Iterations = Max_Iterations_Tag["Max Iterations"]))

    print("\nThe starting number {Starting_Number} has generated the highest number ({Max_Number}) during its iteration number {Iteration}\n" .format(Starting_Number = Max_Number_Tag["Starting Number"], Max_Number = Max_Number_Tag["Max Number"], Iteration = Max_Number_Tag["Iteration"]))
    
    timesTable = [["Total time of execution", str(totalExecutionTime)],
                  ["Total time spent for graphs", str(totalRepresentationTime)]]
    
    print(tabulate(timesTable, headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))

    pyplot.show()
    
    # Export data

    print("\nWould you like to export the data obtained during the computation in an Excel file? (y/n)\n\nWARNING! The new file would be created in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = getcwd()))

    if (yn_input_check() == True):

        timeExportStart = datetime.now()

        print("\n\nPreparing data for export! Please Wait...\n")

        Execution_Table = DataFrame(Execution_Array[1:], index = list(range(1, (Range[1] - Range[0] + 2), 1)), columns = CC.ColumnLabelsArray(Max_Iterations_Tag["Max Iterations"]))

        Dataframes = [DataframeExport(Execution_Table, "Execution Table", True)]

        export_dataframes(Dataframes, fileName = "Collatz Conjecture Results")

        timeExportEnd = datetime.now()

        timeExport = (timeExportEnd - timeExportStart)

        print(tabulate([["Time spent exporting data", str(timeExport)]], headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))

    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()