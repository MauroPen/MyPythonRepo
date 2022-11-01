from numpy import append
from pandas import DataFrame, ExcelWriter
from datetime import date, datetime
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

    while(not(char_input == "y" or char_input == "n")):

        char_input = input()

        if char_input == "y":

            return True

        elif char_input == "n":

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
    "Trials": 1000
}

startDate_Birthdays = date.today().replace(day = 1, month = 1, year = 1922).toordinal()   #Setting the lowest possible birthday admitted

endDate_Birthdays = date.today().replace(day = 31, month = 12, year = 2021).toordinal()   #Setting the highest possible birthday admitted

while (running):

    values = {                                          #Using the default values to initialize the two values
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

    peopleTable = DataFrame(columns = ["Trial", "Person_Id", "Birthday", "Birthday_Match"]) #Creating the table collecting data about all the people generated

    trialTable = DataFrame(columns = ["#People_Sharing_Birthday"]) #Creating the table collecting data about all the trials performed (MIGHT BE EXPANDED)
    
    print("\n\nExecuting trials! Please Wait...\n")
    
    timeExecutionStart = datetime.now()
    
    for trial in trialsList:

        print(" {Status}%" .format(Status = int((trial / values["Trials"]) * 100)), end = "\r")

        trialTable.at[trial, "#People_Sharing_Birthday"] = 0

        people = [0]        #Creating an array of people for each trial, first value is a dummy to align with table indices

        #Creating people
        
        for personId in peopleList:
    
            people = append(people, Person(personId, generate_random_birthday(startDate_Birthdays, endDate_Birthdays)))

            peopleTable.at[(values["People"] * (trial - 1) + personId), "Trial"] = trial

            peopleTable.at[(values["People"] * (trial - 1) + personId), "Person_Id"] = people[personId].id

            peopleTable.at[(values["People"] * (trial - 1) + personId), "Birthday"] = people[personId].birthday

            peopleTable.at[(values["People"] * (trial - 1) + personId), "Birthday_Match"] = people[personId].birthday_match

        #Checking birthdays
        
        for personId in peopleList:                         

            if (people[personId].birthday_match == True):   #If it has a match already then its birthday has already been checked

                break
            
            else:
                
                other_peopleList = peopleList[(personId):]

                for other_personId in other_peopleList:
                    
                    if ((people[personId].birthday.day == people[other_personId].birthday.day) &
                        (people[personId].birthday.month == people[other_personId].birthday.month)):

                        people[personId].birthday_match = True

                        peopleTable.at[(values["People"] * (trial - 1) + personId), "Birthday_Match"] = people[personId].birthday_match

                        people[other_personId].birthday_match = True

                        peopleTable.at[(values["People"] * (trial - 1) + other_personId), "Birthday_Match"] = people[other_personId].birthday_match

        trialTable.at[trial, "#People_Sharing_Birthday"] = count_people_sharing_birthday(people, peopleList)

    timeExecutionEnd = datetime.now()
    
    # Data insights
    
    theoreticalProbability = round((1 - ((factorial(365)) / ((pow(365, values["People"])) * factorial(365 - values["People"])))) * 100, 2)

    experimentalProbability = round(((sum(trialTable.loc[:,"#People_Sharing_Birthday"] > 0)) / values["Trials"]) * 100, 2)
    
    resultsTable = [["Theoretical probability", str(theoreticalProbability) + "%"],
                    ["Experimental result", str((sum(trialTable.loc[:,"#People_Sharing_Birthday"] > 0))) + "/" + str(values["Trials"])],
                    ["Experimental probability", str(experimentalProbability) + "%"],
                    ["Resulting time of execution", str(timeExecutionEnd - timeExecutionStart)]]
    
    print(tabulate(resultsTable, headers = ["Item", "Result"], tablefmt = "github", stralign = "center", showindex = "False"))
    
    # Export data

    print("\n\nWould you like to export the data obtained during the execution in an Excel file? (y/n)\n\nWARNING! The new file would be created in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = getcwd()))

    if (yn_input_check() == True):

        timestampString = datetime.now().strftime("%d_%m_%Y - %H_%M_%S")

        with ExcelWriter ("Birthday Paradox Results ({Timestamp}).xlsx" .format(Timestamp = timestampString)) as writer:

            peopleTable.to_excel(writer, sheet_name = "People", index = True)

            trialTable.to_excel(writer, sheet_name = "Trials", index = True)

            print("\nIn this directory: \"{Current_Working_Directory}\" a file named \"Birthday Paradox Results ({Timestamp}).xlsx\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), Timestamp = timestampString))
    
    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()