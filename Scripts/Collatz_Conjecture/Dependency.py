from numpy import append
from pandas import DataFrame, merge

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

