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
        
#3 - Iterates through peopleList's IDs to count how many people share birthdays. Returns the total number of people sharing birhdays.
def count_people_sharing_birthday(people, peopleList):

    counter = 0

    for personId in peopleList:

        if (people[personId].birthday_match == True):       #Counting how many people share birthday for each trial

            counter += 1
    
    return counter