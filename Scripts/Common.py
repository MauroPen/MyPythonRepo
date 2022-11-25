# 1 - Asks for a y/n input (case insensitive) by the user. Anything else is not accepted.
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

#2 - Asks for an integer by the user, then returns that value. Anything else is not accepted.
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