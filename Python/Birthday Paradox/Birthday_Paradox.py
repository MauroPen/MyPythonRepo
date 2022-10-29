from numpy import append
from pandas import DataFrame
from datetime import date
from random import randint


class Person:

    def __init__(self, Id, Birthday):

        self.id = Id
        self.birthday = Birthday

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

    trialsList = list(range(1, values["Trials"] + 1, 1))

    peopleList = list(range(1, values["People"] + 1, 1))

    peopleTable = DataFrame(columns = ["Trial", "Person_Id", "Birthday"]) #Creating the table collecting data about all the people generated

    for trial in trialsList:

        people = []                #Creating an array of people for each trial

        for personId in peopleList:
    
            people = append(people, Person(personId, generate_random_birthday(startDate_Birthdays, endDate_Birthdays)))

            peopleTable.at[personId, "Trial"] = trial

            peopleTable.at[personId, "Person_Id"] = people[personId - 1].id

            peopleTable.at[personId, "Birthday"] = people[personId - 1].birthday

            print("\n", people[personId - 1].id, people[personId - 1].birthday)