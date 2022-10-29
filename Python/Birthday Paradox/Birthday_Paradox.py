

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

#Setting Default Values

running = bool(True)

defaultValues = {
    "People": 23,
    "Trials": 1000
}

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

    print(values)