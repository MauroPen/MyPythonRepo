# Printing an inputed element an inputed number of times for each line

def iterate(char, num):

    for i in range(1, num + 1):

        print("\n", (char + " ") * i)

def checkPositiveNum(num_input):
    
    print("\nPlease insert the number of iterations that you want to perform:\n")

    while (num_input <= 0):

        num_input = int(input())

        if num_input <= 0:

            print("\nInserted value is not valid, please input a positive number\n")

    return num_input

def end():

    char_input = "Default"

    print("\nEnd of program! Would you like to start over? (Y/N)\n")

    while(not(char_input == "Y" or char_input == "N")):

        char_input = input()

        if char_input == "Y":

            print("\n")

            return 1

        elif char_input == "N":

            return 0

        else:

            print("\nInserted value is not valid, please input Y or N\n")

running = bool(1)

while (running == True):

    char_input = input("Please insert the string or the character that you would like to use:\n\n")

    num_input = checkPositiveNum(num_input := 0)

    iterate(char_input, num_input)

    running = end()
