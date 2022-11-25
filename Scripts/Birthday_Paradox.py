from numpy import array, append, concatenate
from pandas import DataFrame, RangeIndex, ExcelWriter
from datetime import date, datetime, timedelta
from random import randint
from math import factorial
from tabulate import tabulate
from os import getcwd

from Common import yn_input_check, int_input_check
from Birthday_Paradox.Dependency import Person, count_people_sharing_birthday

class Person:

    def __init__(self, Id, Birthday, Birthday_Match):

        self.id = Id
        self.birthday = Birthday
        self.birthday_match = Birthday_Match         #False by default, checked later
        

def count_people_sharing_birthday(people, peopleList):

    counter = 0

    for personId in peopleList:

        if (people[personId].birthday_match == True):       #Counting how many people share birthday for each trial

            counter += 1
    
    return counter

def generate_random_birthday(startDate, endDate):

    return date.fromordinal(randint(startDate, endDate))


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

        print("\nPlease input the number of people that you would like to consider for the computation:\n")
            
        values["People"] = int_input_check()

        print("\nAmazing! Now, please input the number of the trials that you would like to perform:\n")
            
        values["Trials"] = int_input_check()

    #Computation

    trialsList = list(range(1, values["Trials"] + 1, 1))        #List for iterators

    peopleList = list(range(1, values["People"] + 1, 1))        #List for iterators
    
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

        people = [Person(0, date(1900, 1, 1), False)]        #Creating an array of people for each trial, first person is a dummy to align with table indices

        peopleTrialArray = array([[0, 0, date(1900, 1, 1), False]])      #First person (array) is a dummy to align indices, won't be passed in concatenate

        #Creating people

        timeCreationStart = datetime.now()
        
        for personId in peopleList:
    
            people = append(people, Person(personId, generate_random_birthday(startDate_Birthdays, endDate_Birthdays), False))

            peopleTrialArray = concatenate((peopleTrialArray, array([[trial, people[personId].id, people[personId].birthday, False]])))

        timeCreationEnd = datetime.now()

        totalTimeSpentCreatingPeople += (timeCreationEnd - timeCreationStart)

        #Checking birthdays

        timeCheckStart = datetime.now()

        for personId in peopleList:                         

            if (people[personId].birthday_match == True):   #If it already has a match then its birthday has already been checked

                break
            
            else:
                
                other_peopleList = peopleList[(personId):]

                for other_personId in other_peopleList:

                    if (people[personId].birthday.day == people[other_personId].birthday.day):

                        if (people[personId].birthday.month == people[other_personId].birthday.month):
                        
                            people[personId].birthday_match = True

                            peopleTrialArray[personId][3] = people[personId].birthday_match
                            
                            people[other_personId].birthday_match = True

                            peopleTrialArray[other_personId][3] = people[other_personId].birthday_match

        timeCheckEnd = datetime.now()

        totalTimeSpentCheckingBirthdays += (timeCheckEnd - timeCheckStart)

        peopleSharingBirthday = count_people_sharing_birthday(people, peopleList)       #This variable only saves the number of people sharing the birthday for each trial

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

    print("\n\nWould you like to export the data obtained during the execution in an Excel file? (y/n)\n\nWARNING! The new file would be created in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = getcwd()))

    if (yn_input_check() == True):

        timeExportStart = datetime.now()
        
        peopleTable = DataFrame(peopleArray[1:], columns = ["Trial", "Person_Id", "Birthday", "Birthday_Match"], index = RangeIndex(1, (values["People"] * values["Trials"]) + 1, 1))

        trialTable = DataFrame(trialArray[1:], columns = ["#People_Sharing_Birthday", "Time_Execution"], index = RangeIndex(1, (values["Trials"] + 1), 1))

        with ExcelWriter ("Birthday Paradox Results ({Timestamp}).xlsx" .format(Timestamp = timeExportStart.strftime("%d_%m_%Y - %H_%M_%S"))) as writer:

            peopleTable.to_excel(writer, sheet_name = "People", index = True)

            trialTable.to_excel(writer, sheet_name = "Trials", index = True)

            print("\nIn this directory: \"{Current_Working_Directory}\" a file named \"Birthday Paradox Results ({Timestamp}).xlsx\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), Timestamp = timeExportStart))

        timeExportEnd = datetime.now()

        timeExport = (timeExportEnd - timeExportStart)

        print(tabulate([["Time spent exporting data", str(timeExport)]], headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))
    
    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()