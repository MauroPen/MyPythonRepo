import re
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from shared.Common import yn_input_check
from Check_Numbers_Pi.Dependency import number_check, main_computation, check_occurrencies

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

running = True

while(running):

    # Take user input
    print("\nWelcome! Please, input the set of consecutive digits to be found inside pi:\n")
    number = number_check()

    # Running computation
    result = main_computation(number)
    
    if (result["Not Found"] == True):

        print("\nNo match has been found within pi's first million of digits.")

    else:

        print("\n{digits} pi digits have been checked before finding {input}.\nHereby, a snapshot of where to find its first occurrence is provided:\n".format(digits = result["Digits Checked"], input = number))
        print(re.sub(r"^(.{500}).*(.{500})$", "\g<1>...\g<2>", result["Pi Until"][:-len(number)]), end = "")
        print(bcolors.OKGREEN + bcolors.BOLD + str(number) + bcolors.ENDC)

        if (len(result["Pi Until"][:-len(number)]) >= 1000):

            print("\nWould you like to save the whole value of pi until the first occurrence of {combination} in a .txt file in your current directory? y/n".format(combination = number))
            print("WARNING! A new .txt file will be create in your current working directory, which is: {current_working_directory}\n" .format(current_working_directory = os.getcwd()))

            if (yn_input_check()):

                with open("Pi_Until_{combination}.txt".format(combination = number), "w") as file:
                    
                    file.write(result["Pi Until"])
        
        print("\nWould you like to check how many times the combination is present within pi's first million of digits? y/n\n")
        
        if (yn_input_check()):

            print("\nThe combination {combination} has been found {occurrencies} times.".format(combination = number, occurrencies = check_occurrencies(number, result["Digits Checked"])))

    print("\nWould you like to start over? y/n\n")

    running = yn_input_check()