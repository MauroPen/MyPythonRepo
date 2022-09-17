# Collatz Conjecture

def yn_input_check():

    char_input = "Default"

    while(not(char_input == "y" or char_input == "n")):

        char_input = input()

        if char_input == "y":

            return True

        elif char_input == "n":

            return False

        else:

            print("\nThe inserted value is not valid, please input y or n\n")

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

            print("\nThe inserted value is not valid, please input a number higher than 0:\n")

            int_input = -1

#Setting Default Values

running = bool(True)

Default_Range = [1, 50]

while (running == True):

    print("\n\nWelcome to the Collatz Conjecture program!\n\nDo you want to run it in Default Mode? (y/n)\n")

    # Variables settings

    Range = [] 

    Default_mode = yn_input_check()

    if (Default_mode == True):

        Range = Default_Range

    else:

        print("\nPlease input the number that you would like to start the computation from:\n")
        
        Range.append(int_input_check())

        print("\nAmazing! Now, please input the last number of the computation:\n")
        
        Range.append(int_input_check()) #WATCH OUT! It might be lower than the first one (must be checked)

    print(Range, "\n")

    print("\nComputation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()