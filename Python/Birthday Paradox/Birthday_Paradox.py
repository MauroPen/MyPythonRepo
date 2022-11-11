from numpy import array, append, concatenate
from pandas import DataFrame, RangeIndex, ExcelWriter
from datetime import date, datetime, timedelta
from random import randint
from math import factorial
from tabulate import tabulate
from os import getcwd


class Person:

    def __init__(self, Id, Birthday):

        self.id = Id
        self.birthday = Birthday
        self.birthday_match = False         #False by default, checked later

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

            print("\nThe inserted value is not valid, please input an integer number higher than 0:\n")

            int_input = -1

def generate_random_birthday(startDate, endDate):

    return date.fromordinal(randint(startDate, endDate))

def count_people_sharing_birthday(people, peopleList):

    counter = 0

    for personId in peopleList:

        if (people[personId].birthday_match == True):       #Counting how many people share birthday for each trial

            counter += 1
    
    return counter

#Setting Default Values

running = bool(True)

defaultValues = {
    "People": 23,
    "Trials": 1000,
    "Matching_Birthdays": 2     #Meaning "2 or more"
}

startDate_Birthdays = date.today().replace(day = 1, month = 1, year = 1922).toordinal()   #Setting the lowest possible birthday admitted

endDate_Birthdays = date.today().replace(day = 31, month = 12, year = 2021).toordinal()   #Setting the highest possible birthday admitted

while (running):

    values = {                                  #Using the default values to initialize the first two values
        "People": defaultValues["People"],
        "Trials": defaultValues["Trials"],
        "Matching_Birthdays": -1                #Here it's different to allow cycling in case of input error
    }

    print("\n\nWelcome to the Birthday Paradox program!\n\nDo you want to run it in Default Mode? (y/n)\n")

    defaultMode = yn_input_check()

    if (not defaultMode):

        print("\nPlease input the number of people that you would like to consider for the computation:\n")
            
        values["People"] = int_input_check()

        print("\nAmazing! Now, please input the number of the trials that you would like to perform:\n")
            
        values["Trials"] = int_input_check()

        print("\nFinally, please input for how many people sharing the same birthday you would like to compute the probability (Default: 2):\n")
            
        while (values["Matching_Birthdays"] < 0):
        
            values["Matching_Birthdays"] = int_input_check()

            if (values["Matching_Birthdays"] > values["People"]):

                print("\nThe number of people sharing the same birthday cannot be higher than the number of people considered. Please, input a number lower or equal than {People}\n" .format(People = values["People"]))

                values["Matching_Birthdays"] = -1

    else:

        values["Matching_Birthdays"] = defaultValues["Matching_Birthdays"]

    #Computation

    trialsList = list(range(1, values["Trials"] + 1, 1))        #List for iterators

    peopleList = list(range(1, values["People"] + 1, 1))        #List for iterators
    
    peopleArray = array([[0, 0, date(1900, 1,1), False]])       #An array collecting the data about all the people generated, first person (array) is a dummy to align indices

    trialArray = array([[0, timedelta(seconds = 0)]])           #An array collecting data about all the trials performed (MIGHT BE EXPANDED), first trial (array) is a dummy to align indices

    totalPositiveTrials = 0                                     #Tracks the number of trials with matching birthdays
    
    print("\n\nExecuting trials! Please Wait...\n")

    timeTrial = timedelta(seconds = 0)
    
    totalTimeSpentCreatingPeople = timedelta(seconds = 0)

    totalTimeSpentCheckingBirthdays = timedelta(seconds = 0)

    timeExecution = timedelta(seconds = 0)
    
    timeExecutionStart = datetime.now()

    for trial in trialsList:

        print(" {Status}%" .format(Status = int((trial / values["Trials"]) * 100)), end = "\r")

        timeTrialStart = datetime.now()

        people = [Person(0, date(1900, 1, 1))]        #Creating an array of people for each trial, first person is a dummy to align with table indices

        peopleTrialArray = array([[0, 0, date(1900, 1, 1), False]])      #First person (array) is a dummy to align indices, won't be passed in concatenate

        #Creating people

        timeCreationStart = datetime.now()
        
        for personId in peopleList:
    
            people = append(people, Person(personId, generate_random_birthday(startDate_Birthdays, endDate_Birthdays)))

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

        peopleArray = concatenate((peopleArray, peopleTrialArray[1:]))

        trialArray = concatenate((trialArray, array([[count_people_sharing_birthday(people, peopleList), timedelta(seconds = 0)]])))

        if (trialArray[trial][0] > 0):

            totalPositiveTrials += 1

        timeTrialEnd = datetime.now()

        timeTrial = (timeTrialEnd - timeTrialStart)

        trialArray[trial][1] = (timeTrial.seconds * 1000000 + timeTrial.microseconds)

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