

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