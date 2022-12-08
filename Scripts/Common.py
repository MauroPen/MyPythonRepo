from os import getcwd
from pandas import ExcelWriter
from datetime import datetime

# 1 - Asks for a y/n input (case insensitive) by the user. Anything else is not accepted.
def yn_input_check():

    char_input = ""

    while(not(char_input == "y" or char_input == "Y" or char_input == "n" or char_input == "N")):

        char_input = input()

        if (char_input == "y" or char_input == "Y"):

            return True

        elif (char_input == "n" or char_input == "N"):

            return False

        else:

            print("\nThe inserted value is not valid, please input \"y\" or \"n\"\n")

#2 - Asks for an integer by the user, then returns that value. Anything else is not accepted.
def int_input_check():

    int_input = -1

    while (int_input < 0):

        try:
            
            int_input = int(input())
    
            while(int_input <= 0):

                print("\nThe inserted value is not valid, please input a number higher than 0:\n")

                int_input = int(input())

            return int_input
        
        except:

            print("\nThe inserted value is not valid, please input an integer number higher than 0:\n")

            int_input = -1

#3 - An entity used to export dataframes
class DataframeExport:

    def __init__(self, Table, Sheet_Name, Index):

        self.Table = Table
        self.Sheet_Name = Sheet_Name
        self.Index = Index              #Boolean

#4 - Exports pandas dataframes in an Excel file with multiple sheets
def export_dataframes(dataframes, fileName):        # "dataframes" is meant to be an array of DataframeExport (#3) objects

    fileName = fileName + " (" + datetime.now().strftime("%d_%m_%Y - %H_%M_%S") + ").xlsx"
    
    with ExcelWriter (fileName) as writer:

            for dataframe in range(0, len(dataframes), 1):

                dataframes[dataframe].Table.to_excel(writer, sheet_name = dataframes[dataframe].Sheet_Name, index = dataframes[dataframe].Index)

            print("\nIn this directory: \"{Current_Working_Directory}\" a file named \"{File_Name}\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), File_Name = fileName))
