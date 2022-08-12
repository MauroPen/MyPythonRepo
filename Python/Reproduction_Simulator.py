# Reproduction Simulator
from numpy import random, mean
from tabulate import tabulate
from matplotlib import pyplot

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

def compute_mean(Tab, Period, Starting_Value):

    Avg_Array = [Starting_Value]

    for i in range(0, Period + 1, 1):

        Avg_Values = [value[i] for value in Tab]
        
        Avg_Array[i] = mean(Avg_Values)

        Avg_Array.append([])
    
    del Avg_Array[-1]

    return Avg_Array


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

    Period_Arr = list(range(0, Period + 1, 1)) #Indexes the periods, necessary for plots

    N_Tab = [] #Collects the resulting N each time for each iteration

    D_Tab = [] #Collects the resuling D each time for each iteration

    pyplot.title("Simulation Results")
    pyplot.xlabel("Period") 
    pyplot.ylabel("Population") 

    for i in range(1, Repeat + 1, 1): #Iterating the same simulation 30 times

        N_Tab.append([])

        D_Tab.append([])

        N_Arr = [Starting_N] #Collects the resulting N each time

        D_Arr =  [0] #Collects the resuling D each time

        for j in range(1, Period + 1, 1):

            N = N_Arr[j - 1] #Sets the starting population for calculation

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
            
            D_Arr.append(D) #Updates with the new values

            N_Arr.append(N) #Updates with the new values
            
            #print("\nProcessing! Please Wait...\n\nCurrent Day: ", j, "/", Period)
        
        N_Tab[i - 1] = N_Arr
        
        D_Tab[i - 1] = D_Arr
        
        pyplot.plot(Period_Arr, N_Arr, linestyle = ":")

    #print(N_Tab, D_Tab)

    Avg_N = compute_mean(N_Tab, Period, Starting_N)

    Avg_D = compute_mean(D_Tab, Period, 0)

    #print(Avg_N, "\n", Avg_D)

    pyplot.plot(Period_Arr, Avg_N)

    """
    # Results Presentation

    print("\n")
    print(tabulate(list(zip(N_Arr, D_Arr)), headers = ["Period", "Population", "Delta"], showindex = True, tablefmt = "github", numalign = "center"))

    print("\nInitial Population: ", N_Arr[0])
    print("\nBirth Rate set: ", b)
    print("\nDeath Rate set: ", d)
    print("\nFinal_Population: ", N_Arr[Period])
    print("\nTotal Delta: ", sum(D_Arr))

    """
    pyplot.show()

    print("\n\nSimulation ended!\n\nDo you want to start over? (Y/N)\n")
    
    running = yn_input_check()