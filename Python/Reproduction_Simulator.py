# Reproduction Simulator

def end():

    char_input = "Default"

    print("\n\nSimulation ended!\n\nDo you want to start over? (Y/N)\n")

    while(not(char_input == "Y" or char_input == "N")):

        char_input = input()

        if char_input == "Y":

            print("\n")

            return 1

        elif char_input == "N":

            return 0

        else:

            print("\nInserted value is not valid, please input Y or N\n")


from numpy import random
from tabulate import tabulate
from matplotlib import pyplot

running = bool(True)

while (running == True):

    print("Welcome to the Reproduction Simulator!\n")

    # Variables settings

    Starting_N = int(input("\nPlease input the Inital Number of Population that you want to set:\n", )) # Exceptions to be added

    Period = int(input("\nAmazing! Now, please input the length of the Period of time that you want to consider for the simulation:\n")) # Exceptions to be added

    b = float(input("\nGreat! Now, please input the Birth Rate:\n", )) # Exceptions to be added

    d = float(input("\nAwesome! Now, please input the desired Death Rate: \n", )) # Exceptions to be added

    c = float(input("\nFinally, please input the Crowding Coefficient. \nPAY ATTENTION! This coefficient will positively affect the Death Rate of your population for each period (default_value: 0.001):\n"), )

    # Computation

    Period_Tab = list(range(0, Period + 1, 1)) #Indexes the periods, necessary for plots

    pyplot.title("Simulation Results") 
    pyplot.xlabel("Period") 
    pyplot.ylabel("Population") 

    for i in range(1, 31, 1): #Iterating the same simulation 30 times. Must become a parameter

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

    running = end()