from datetime import date
from random import randint

#1 - An entity describing each individual 
class Person:

    def __init__(self, Id, Birthday, Birthday_Match):

        self.id = Id
        self.birthday = Birthday
        self.birthday_match = Birthday_Match

#2 - Generates a random birth date
def generate_random_birth_date(startDate, endDate):

    return date.fromordinal(randint(startDate, endDate))

#3 - Checks and marks people sharing birthday in a specific set of people
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
        
#4 - Iterates through peopleList's IDs to count how many people share birthdays. Returns the total number of people sharing birhdays.
def count_people_sharing_birthday(people, peopleList):

    counter = 0

    for personId in peopleList:

        if (people[personId].birthday_match == True):       #Counting how many people share birthday for each trial

            counter += 1
    
    return counter