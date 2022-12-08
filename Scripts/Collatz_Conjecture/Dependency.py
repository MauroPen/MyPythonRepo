from numpy import array, where, concatenate, append, full
from pandas import DataFrame, merge

#1 - The main computation of the Collatz Conjecture program
def mainComputation(Range, Max_Number_Tag, Max_Iterations_Tag):

    Execution_Array = array([[0, [0]]], dtype = object)       #Initialized with meaningless values that will be ignored

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

    return (Execution_Array, Max_Number_Tag, Max_Iterations_Tag)

#2 - Adds as many "0" as necessary to make every array the same length
def normalizeArray(Array, Range, Max_Iterations):

    print("\n\nPreparing data for plotting! Please Wait...\n")

    Final_Array = array(full(shape = (1, Max_Iterations + 1), fill_value = 0))

    for i in range(1, (Range[1] - Range[0] + 2), 1):

        print(" {Status}%" .format(Status = int((i / (Range[1] - Range[0] + 1)) * 100)), end = "\r")
        
        while (len(Array[i][1][0]) != Max_Iterations + 1):

            Array[i][1][0] = append(Array[i][1][0], int(0))

        Final_Array = concatenate((Final_Array, array([Array[i][1][0]])))

    return Final_Array

#3 - Generates the column labels necessary for the DataFrame to export
def ColumnLabelsArray(Max_Iterations):

    ColumnLabels = array("Starting Number")

    for j in range(1, Max_Iterations + 1, 1):
        
        ColumnLabels = append(ColumnLabels, "Iteration " + str(j))
        
    return ColumnLabels

#DEPRECATED

#1 - Adds as many "0" as necessary to make every array the same length
def normalizeValues(Table, Range, Max_Iterations):

    print("\n\nPreparing data for plotting! Please Wait...\n")

    for i in range(1, (Range[1] - Range[0] + 2), 1):

        print(" {Status}%" .format(Status = int((i / (Range[1] - Range[0] + 1)) * 100)), end = "\r")
        
        while (len(Table.at[i, "Obtained Values"]) != Max_Iterations + 1):

            Table.at[i, "Obtained Values"] = append(Table.at[i, "Obtained Values"], int(0))

    return Table

#2 - Transforms arrays into columns before exporting data
def transformArraysIntoColumns(Table, Range, Max_Iterations):

    Transform_Array_Into_DataFrame = DataFrame(data = Table["Obtained Values"].values.tolist(), dtype = int, index = list(range(1, (Range[1] - Range[0] + 2), 1)), columns = ColumnLabelsArray(Max_Iterations))

    Table = merge(Table.drop(columns = ["Starting Number", "Obtained Values"]), Transform_Array_Into_DataFrame, how = "inner", left_index = True, right_index = True)
    
    return Table