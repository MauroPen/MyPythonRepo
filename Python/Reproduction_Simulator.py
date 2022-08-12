# Reproduction Simulator

def int_input_check():

    int_input = int(input())
    
    while(int_input < 0):

        print("\nThe inserted value is not valid, please input a number higher than 0:\n")

        int_input = int(input())

    return (int_input)


def float_input_check():

    float_input = float(input())

    while (not(float_input >= 0 and float_input <= 1)):

        print("\nThe inserted value is not valid, please input a number between 0 and 1:\n")

        float_input = float(input())

    return (float_input)


def yn_input_check():

    char_input = "Default"

    while(not(char_input == "Y" or char_input == "N")):

        char_input = input()

        if char_input == "Y":

            print("\n")

            return 1

        elif char_input == "N":

            return 0

        else:

            print("\nThe inserted value is not valid, please input Y or N\n")


from numpy import random
from tabulate import tabulate
from matplotlib import pyplot

running = bool(True)

while (running == True):

    print("Welcome to the Reproduction Simulator!\n\nDo you want to run in Default Mode? (Y/N)\n")

    # Variables settings  

    Default_mode = yn_input_check()
    
    if (Default_mode == True):

        Starting_N = 50

        Period = 30

        b = 0.2

        d = 0.1

        c = 0.001

        Repeat = 30

    else:

        print("\nPlease input the Inital Number of Population that you want to set:\n")
        
        Starting_N = int_input_check()

        print("\nAmazing! Now, please input the length of the Period of time that you want to consider for the simulation:\n")
        
        Period = int_input_check()

        print("\nGreat! Now, please input the Birth Rate:\n")
        
        b = float_input_check()

        print("\nAwesome! Now, please input the desired Death Rate:\n")

        d = float_input_check()

        print("\n\nFantastic! Now, please input the Crowding Coefficient. \n\nPAY ATTENTION! This coefficient will positively affect the Death Rate of your population for each period (recommended value: 0.001):\n")

        c = float_input_check()

        print("\nFinally, please input the number of times that you want this simulation to be repeated:\n")

        Repeat = int_input_check()

    # Computation

    Period_Tab = list(range(0, Period + 1, 1)) #Indexes the periods, necessary for plots

    pyplot.title("Simulation Results") 
    pyplot.xlabel("Period") 
    pyplot.ylabel("Population") 

    for i in range(1, Repeat + 1, 1): #Iterating the same simulation 30 times

        N_Tab = [Starting_N] #Collects the resulting N each time for each iteration

        D_Tab =  [0] #Collects the resuling D each time for each iteration

        for j in range(1, Period + 1, 1):

            N = N_Tab[j - 1] #Sets the starting population for calculation

            D = 0 #Collects the Delta each time

            for k in range(1, N + 1, 1):

                br = random.binomial(1, b, 1)[0]

                dr = random.binomial(1, d + (c * N), 1)[0]

                if (br == 1):

                    D += 1

                elif (dr == 1):

                    D -= 1

                #print("\nProcessing! Please Wait...\n\nCurrent Person Evaluated: ", k, "/", N)

            N += D
            
            D_Tab.append(D) #Updates table

            N_Tab.append(N) #Updates table

        pyplot.plot(Period_Tab, N_Tab, linestyle = ":")

        #print("\nProcessing! Please Wait...\n\nCurrent Day: ", j, "/", Period)

    """
    # Results Presentation

    print("\n")
    print(tabulate(list(zip(N_Tab, D_Tab)), headers = ["Period", "Population", "Delta"], showindex = True, tablefmt = "github", numalign = "center"))

    print("\nInitial Population: ", N_Tab[0])
    print("\nBirth Rate set: ", b)
    print("\nDeath Rate set: ", d)
    print("\nFinal_Population: ", N_Tab[Period])
    print("\nTotal Delta: ", sum(D_Tab))

    """
    pyplot.show()

    print("\n\nSimulation ended!\n\nDo you want to start over? (Y/N)\n")
    
    running = yn_input_check()