# Reproduction Simulator

from numpy import random, mean, linspace
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

    while(not(char_input == "y" or char_input == "n")):

        char_input = input()

        if char_input == "y":

            return 1

        elif char_input == "n":

            return 0

        else:

            print("\nThe inserted value is not valid, please input y or n\n")


def compute_mean(Tab, Period, Starting_Value):

    Avg_Array = [Starting_Value]

    for i in range(0, Period + 1, 1):

        Avg_Values = [value[i] for value in Tab]
        
        Avg_Array[i] = mean(Avg_Values)

        Avg_Array.append([])
    
    del Avg_Array[-1]

    return Avg_Array

#Setting Default Values

running = bool(True)

default_Starting_N = int(50)

default_Period = int(30)

default_b = float(0.2)

default_d = float(0.1)

default_c = float(0.001)

default_Repeat = int(30)

while (running == True):

    print("\n\nWelcome to the Reproduction Simulator!\n\nDo you want to run in Default Mode? (y/n)\n")

    # Variables settings  

    Default_mode = yn_input_check()
    
    if (Default_mode == True):

        Starting_N = default_Starting_N

        Period = default_Period

        b = default_b

        d = default_d

        c = default_c

        Repeat = default_Repeat

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

        print("\nDo you want these settings to become the Default Settings for the next iterations? (y/n)\n")

        Edit_default = yn_input_check()

        if (Edit_default == True):

            default_Starting_N = Starting_N
            default_Period = Period
            default_b = b
            default_d = d
            default_c = c
            default_Repeat = Repeat

    # Computation

    Period_Arr = list(range(0, Period + 1, 1)) #Indexes the periods, necessary for plots

    N_Tab = [] #Collects the resulting N each time for each iteration

    D_Tab = [] #Collects the resuling D each time for each iteration

    # Plot Simulation Results

    fig, axs = pyplot.subplots(2, sharex = True)
    axs[0].set_title("Simulation Results - Population Growth Overtime") 
    axs[0].set_ylabel("Population")
    axs[1].set_title("Simulation Results - Delta Population Overtime")
    axs[1].set_xlabel("Period") 
    axs[1].set_ylabel("Delta")

    print("\n\nProcessing! Please Wait...\n")

    for i in range(1, Repeat + 1, 1): #Iterating the same simulation multiple times

        print("Current Iteration: {} / {}" .format(i, Repeat), end = "\r")

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

                if (dr == 1):

                    D -= 1

            N += D
            
            D_Arr.append(D) #Updates with the new values

            N_Arr.append(N) #Updates with the new values
        
        N_Tab[i - 1] = N_Arr
        
        D_Tab[i - 1] = D_Arr
        
        axs[0].plot(Period_Arr, N_Arr, linestyle = ":")

        axs[1].plot(Period_Arr, D_Arr, linestyle = ":")

    Avg_N = compute_mean(N_Tab, Period, Starting_N)

    Avg_D = compute_mean(D_Tab, Period, 0)

    # Plot Average Simulation Results

    axs[0].plot(Period_Arr, Avg_N, linewidth = 3, color = "k", label = "Average Population Growth")

    axs[1].plot(Period_Arr, Avg_D, linewidth = 3, color = "k", label = "Average Delta Population")
    
    # Plot Theoretical Population Growth

    yn = [Starting_N]

    for j in range(1, Period + 1, 1):

        yn.append(yn[j - 1] + yn[j - 1] * (b - d - c * yn[j - 1]))

    axs[0].plot(Period_Arr, yn, linewidth = 2, color = "m",  label = "Expected Population Growth")

    axs[0].legend(loc = "upper left", fontsize = 6)
    
    # Plot Theoretical Delta Population Function

    yd = [0]

    for j in range(1, Period + 1, 1):

        yd.append(yn[j] - yn[j - 1])

    axs[1].plot(Period_Arr, yd, linewidth = 2, color = "m", label = "Expected Delta Population")

    axs[1].legend(loc = "upper left", fontsize = 6)
    
    # Results Presentation

    print("\n\n\nInitial Population: ", Starting_N)
    print("\nLength of Period set: ", Period)
    print("\nBirth Rate set: ", b)
    print("\nDeath Rate set: ", d)
    print("\nCrowding Coefficient set: ", c)
    print("\nNumber of iterations done: ", Repeat)

    print("\n\nAverage Final Population: ", Avg_N[Period])
    print("\nTheoretical Final Population: ", yn[Period])
    print("\nAverage Delta per Period: ", mean(Avg_D))
    print("\nTheoretical Delta per Period: ", yd[Period])

    print("\n\nAverage Population per Period: \n")
    print(tabulate(list(zip(Period_Arr, Avg_N)), headers = ["Period", "Average Population"], tablefmt = "github", numalign = "center"))
    
    pyplot.show()

    print("\n\nSimulation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()


"""""
#This piece of code plots the theoretical variation of the Delta in function of the Population

xd = linspace(0, ((b-d)/c), 10000)

yd = xd * (b - d - c * xd)

axs[1][1].set_title("Theoretical Delta Function")
axs[1][1].set_xlabel("Population") 
axs[1][1].set_ylabel("Delta")

axs[1][1].plot(xd, yd)

"""