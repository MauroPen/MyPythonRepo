import math_pi

from Common import yn_input_check
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
    print("\nWelcome! Please, input the set of consecutive digits to be found inside pi: ", end = "")
    number = number_check()

    # Running computation
    result = main_computation(number)
    
    if (result["Not Found"] == True):

        print("\nNo match has been found within pi's first million of digits.")

    else:

        print("\n{digits} pi digits have been checked to find {input}.\nHereby, all pi digits until the first occurrence of {input} are printed:\n".format(digits = result["Digits Checked"], input = number))
        print(result["Pi Until"][:-len(number)], end = "")
        print(bcolors.OKGREEN + bcolors.BOLD + str(number) + bcolors.ENDC)

        print("\nWould you like to check how many times the combination is present within pi's first million of digits? y/n")
        
        if (yn_input_check()):

            print("\nThe combination {Combination} has been found {Occurrencies} times.".format(Combination = number, Occurrencies = check_occurrencies(number, result["Digits Checked"])))

    print("\nWould you like to start over? y/n")
    running = yn_input_check()