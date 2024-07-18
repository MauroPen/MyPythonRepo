import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from numpy import array, concatenate
from pandas import DataFrame, RangeIndex
from datetime import date, datetime, timedelta
from math import factorial
from tabulate import tabulate



from shared.Common import yn_input_check, int_input_check, DataframeExport, export_dataframes

import Dependency as BP

#Setting Default Values

running = bool(True)

defaultValues = {
    "People": 23,
    "Trials": 1000
}

startDate_Birthdays = date.today().replace(day = 1, month = 1, year = 1922).toordinal()   #Setting the lowest possible birthday admitted

endDate_Birthdays = date.today().replace(day = 31, month = 12, year = 2021).toordinal()   #Setting the highest possible birthday admitted

while (running):

    values = {                                  #Using the default values to initialize the first two values
        "People": defaultValues["People"],
        "Trials": defaultValues["Trials"]
    }

    print("\n\nWelcome to the Birthday Paradox program!\n\nDo you want to run it in Default Mode? (y/n)\n")

    defaultMode = yn_input_check()

    if (not defaultMode):

        print("\nPlease input the number of people that you would like to consider for the computation (for reference, default is 23):\n")
            
        values["People"] = int_input_check()

        print("\nAmazing! Now, please input the number of the trials that you would like to perform (for reference, default is 1000):\n")
            
        values["Trials"] = int_input_check()

    #Computation

    trialsList = tuple(range(1, values["Trials"] + 1, 1))       #List for iterators (type is "tuple" because it is not changing during execution and is more efficient)

    peopleList = tuple(range(1, values["People"] + 1, 1))       #List for iterators (type is "tuple" because it is not changing during execution and is more efficient)
    
    peopleArray = array([[0, 0, date(1900, 1,1), False]])       #An array collecting the data about all the people generated, first person (array) is a dummy to align indices

    trialArray = array([[0, timedelta(seconds = 0)]])           #An array collecting data about all the trials performed, first trial (array) is a dummy to align indices

    trial500Array = array([[0, timedelta(seconds = 0)]])        #An array collecting data about each 500 trial performed, then moved to trialArray
    
    totalPositiveTrials = 0                                     #Tracks the number of trials with matching birthdays
    
    print("\n\nExecuting trials! Please Wait...\n")

    timeTrial = timedelta(seconds = 0)
    
    totalTimeSpentCreatingPeople = timedelta(seconds = 0)

    totalTimeSpentCheckingBirthdays = timedelta(seconds = 0)

    timeExecution = timedelta(seconds = 0)
    
    timeExecutionStart = datetime.now()

    for trial in trialsList:

        if ((trial % 500) == 0):        #Moving the data from trial500Array to trialArray each 500 trials, then reinitializing the first one

            trialArray = concatenate((trialArray, trial500Array[1:]))

            trial500Array = array([[0, timedelta(seconds = 0)]])

        print(" {Status}%" .format(Status = int((trial / values["Trials"]) * 100)), end = "\r")

        timeTrialStart = datetime.now()

        people = [BP.Person(0, date(1900, 1, 1), False)]        #Creating an array of people for each trial, first person is a dummy to align with table indices

        peopleTrialArray = array([[0, 0, date(1900, 1, 1), False]])      #First person (array) is a dummy to align indices, won't be passed in concatenate

        #Creating people

        timeCreationStart = datetime.now()

        (people, peopleTrialArray) = BP.create_people(people, peopleTrialArray, peopleList, trial, startDate_Birthdays, endDate_Birthdays)
        
        timeCreationEnd = datetime.now()

        totalTimeSpentCreatingPeople += (timeCreationEnd - timeCreationStart)

        #Checking birthdays

        timeCheckStart = datetime.now()

        (people, peopleTrialArray) = BP.check_people_sharing_birthday(people, peopleTrialArray, peopleList)

        timeCheckEnd = datetime.now()

        totalTimeSpentCheckingBirthdays += (timeCheckEnd - timeCheckStart)

        peopleSharingBirthday = BP.count_people_sharing_birthday(people, peopleList)       #This variable only saves the number of people sharing the birthday for each trial

        if (peopleSharingBirthday > 0):

            totalPositiveTrials += 1
        
        peopleArray = concatenate((peopleArray, peopleTrialArray[1:]))

        timeTrialEnd = datetime.now()

        timeTrial = (timeTrialEnd - timeTrialStart)

        trial500Array = concatenate((trial500Array, array([[peopleSharingBirthday, (timeTrial.seconds * 1000000 + timeTrial.microseconds)]])))

    if ((len(trial500Array)) > 1):        #Checking whether all the data have been moved from trial500Array to trialArray

            trialArray = concatenate((trialArray, trial500Array[1:]))
    
    timeExecutionEnd = datetime.now()

    timeExecution = (timeExecutionEnd - timeExecutionStart)
    
    # Data insights
    
    theoreticalProbability = round((1 - ((factorial(365)) / ((pow(365, values["People"])) * factorial(365 - values["People"])))) * 100, 2)

    experimentalProbability = round(((totalPositiveTrials / values["Trials"]) * 100), 2)
    
    resultsTable = [["Theoretical probability", str(theoreticalProbability) + "%"],
                    ["Experimental result", str(totalPositiveTrials) + "/" + str(values["Trials"])],
                    ["Experimental probability", str(experimentalProbability) + "%"]]

    timesTable = [["Total time spent creating people", str(totalTimeSpentCreatingPeople)],
                  ["Total time spent checking birthdays", str(totalTimeSpentCheckingBirthdays)],
                  ["Total time of execution", str(timeExecution)]]
    
    print(tabulate(resultsTable, headers = ["Item", "Result"], tablefmt = "github", stralign = "center", showindex = "False"))

    print("\n")

    print(tabulate(timesTable, headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))
    
    # Export data

    print("\n\nWould you like to export the data obtained during the execution in an Excel file? (y/n)\n\nWARNING! The new file would be created in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = os.getcwd()))

    if (yn_input_check() == True):

        timeExportStart = datetime.now()
        
        peopleTable = DataFrame(peopleArray[1:], columns = ["Trial", "Person_Id", "Birthday", "Birthday_Match"], index = RangeIndex(1, (values["People"] * values["Trials"]) + 1, 1))

        trialTable = DataFrame(trialArray[1:], columns = ["#People_Sharing_Birthday", "Time_Execution"], index = RangeIndex(1, (values["Trials"] + 1), 1))

        dataframes = [DataframeExport(peopleTable, "People", True), DataframeExport(trialTable, "Trials", True)]
        
        export_dataframes(dataframes, fileName = "Birthday Paradox Results")

        timeExportEnd = datetime.now()

        timeExport = (timeExportEnd - timeExportStart)

        print(tabulate([["Time spent exporting data", str(timeExport)]], headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))
    
    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()