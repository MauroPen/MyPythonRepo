from numpy import array, full, concatenate, append
from pandas import DataFrame, merge

#1 - Adds as many "0" as necessary to make every array the same length
def normalizeArray(Array, Range, Max_Iterations):

    print("\n\nPreparing data for plotting! Please Wait...\n")

    Final_Array = array(full(shape = (1, Max_Iterations + 1), fill_value = 0))

    for i in range(1, (Range[1] - Range[0] + 2), 1):

        print(" {Status}%" .format(Status = int((i / (Range[1] - Range[0] + 1)) * 100)), end = "\r")
        
        while (len(Array[i][1][0]) != Max_Iterations + 1):

            Array[i][1][0] = append(Array[i][1][0], int(0))

        Final_Array = concatenate((Final_Array, array([Array[i][1][0]])))

    return Final_Array

#2 - Generates the column labels necessary for the DataFrame to export
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