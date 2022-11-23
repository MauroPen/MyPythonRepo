
# 1 - yn_input_check: asks for a y/n input (case insensitive) by the user. Anything else is not accepted.
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

#2 - int_input_check: asks for an integer by the user, then returns that value. Anything else is not accepted.
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

class Person:

    def __init__(self, Id, Birthday):

        self.id = Id
        self.birthday = Birthday
        self.birthday_match = False         #False by default, checked later
        

def count_people_sharing_birthday(people, peopleList):

    counter = 0

    for personId in peopleList:

        if (people[personId].birthday_match == True):       #Counting how many people share birthday for each trial

            counter += 1
    
    return counter

