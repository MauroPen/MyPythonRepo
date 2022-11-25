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
