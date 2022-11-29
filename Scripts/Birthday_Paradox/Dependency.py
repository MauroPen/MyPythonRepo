from numpy import array, append, concatenate
from datetime import date
from random import randint

#1 - An entity describing each individual 
class Person:

    def __init__(self, Id, Birthday, Birthday_Match):

        self.id = Id
        self.birthday = Birthday
        self.birthday_match = Birthday_Match

#2 - Generates the necessary people to run a trial
def create_people(people, peopleTrialArray, peopleList, trial, startDate_Birthdays, endDate_Birthdays):

    for personId in peopleList:
    
            people = append(people, Person(personId, generate_random_birth_date(startDate_Birthdays, endDate_Birthdays), False))         #Birthday_Match is False by default and is checked later

            peopleTrialArray = concatenate((peopleTrialArray, array([[trial, people[personId].id, people[personId].birthday, False]])))
    
    return (people, peopleTrialArray)

#3 - Generates a random birth date
def generate_random_birth_date(startDate, endDate):

    return date.fromordinal(randint(startDate, endDate))

#4 - Checks and marks people sharing birthday in a specific set of people
def check_people_sharing_birthday(people, peopleTrialArray, peopleList):

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

    return (people, peopleTrialArray)
        
#5 - Iterates through peopleList's IDs to count how many people share birthdays. Returns the total number of people sharing birhdays.
def count_people_sharing_birthday(people, peopleList):

    counter = 0

    for personId in peopleList:

        if (people[personId].birthday_match == True):       #Counting how many people share birthday for each trial

            counter += 1
    
    return counter