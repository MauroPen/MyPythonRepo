# Reproduction Simulator

from math import isnan
from tkinter import Y
from numpy import random, mean, linspace, full, unique
from tabulate import tabulate
from matplotlib import pyplot, gridspec
from pandas import DataFrame, Series
from sys import warnoptions

if not warnoptions:

    from warnings import simplefilter

    simplefilter("ignore")


def int_input_check():

    int_input = int(input())
    
    while(int_input < 0):

        print("\nThe inserted value is not valid, please input a number higher than 0:\n")

        int_input = int(input())

    return int_input


def float_input_check():

    float_input = float(input())

    while (not(float_input >= 0 and float_input <= 1)):

        print("\nThe inserted value is not valid, please input a number between 0 and 1:\n")

        float_input = float(input())

    return float_input


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


def compute_mean(Tab, Period, Starting_Value):

    Avg_Array = [Starting_Value]

    for i in range(1, Period + 1, 1):

        Avg_Array.append([])

        Avg_Array[i] = mean(Tab["Period " + str(i)])

    return Avg_Array


def compute_unique_Tab_Values(Tab, Period, Repeat): # This is a function extracting only the values for N obtained during the simulation

    Tab_Values = []

    for i in range(0, Period + 1, 1):

        for j in range(1, Repeat + 1, 1):
            
            Tab_Values.append(Tab["Period " + str(i)][j])

    return unique(Tab_Values)


def compute_avg_Delta_Population(Unique_Array, Tab1, Tab2, Period, Repeat):

    Avg_Values = []

    print("\n\nI am now computing the Average Delta in function of the Population from the simulation results\n")

    for i in range(0, int(max(Unique_Array)) + 1, 1):

        print("Please, Wait... Current Iteration: {} / {}" .format(i, int(max(Unique_Array))), end = "\r")

        collector = [] #Collects the values of D to average for each N

        for j in range(0, Period, 1): # Only "Period" because there is no data available for the last Period of simulation

            for k in range(1, Repeat + 1, 1):
            
                if (Tab1["Period " + str(j)][k] == i):
                    
                    collector.append(Tab2["Period " + str(j + 1)][k])
            
        if (isnan(mean(collector)) == True):

            Avg_Values.append(0)

        else:

            Avg_Values.append(mean(collector))

    return Avg_Values


#Setting Default Values

running = bool(True)

default_Starting_N = int(25)

default_Period = int(50)

default_b = float(0.2)

default_d = float(0.1)

default_c = float(0.001)

default_Repeat = int(50)

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

        print("\n\nFantastic! Now, please input the Crowding Coefficient. \n\nWARNING! This coefficient will positively affect the Death Rate of your population for each period (recommended value: 0.001):\n")

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

    # Computation of Average Delta in function of the Population? (y/n)
    
    print("\n\nDo you want to compute the Average Delta in function of the Population too? (y/n)\n\nWARNING! This computation may require longer times of execution of the program.\n")

    Compute_Avg_Delta_Population = yn_input_check()

    # Computation

    Period_Arr = list(range(0, Period + 1, 1)) #Indexes the periods, necessary for plots

    N_Tab = DataFrame({"Period 0": full(Repeat, Starting_N)}, dtype = int, index = list(range(1, Repeat + 1, 1))) #Collects the resulting N each time for each iteration

    D_Tab = DataFrame({"Period 0": full(Repeat, 0)}, dtype = int, index = list(range(1, Repeat + 1, 1))) #Collects the resulting D each time for each iteration

    for i in range(1, Period + 1, 1) :
        
        N_Tab["Period " + str(i)] = Series(dtype = int)
        
        D_Tab["Period " + str(i)] = Series(dtype = int)

    # Plot Simulation Results

    if (Compute_Avg_Delta_Population == True):

        gs = gridspec.GridSpec(2, 2)

    else:

        gs = gridspec.GridSpec(2, 1)

    fig = pyplot.figure()
    ax1 = fig.add_subplot(gs[0, 0])
    pyplot.setp(ax1.get_xticklabels(), visible = False) #Hiding ticks for readability
    ax1.set_title("Population Growth Overtime") 
    ax1.set_ylabel("Population")

    ax2 = fig.add_subplot(gs[1, 0], sharex = ax1)
    ax2.set_title("Delta Population Overtime")
    ax2.set_xlabel("Period")
    ax2.set_ylabel("Delta")

    print("\n\nProcessing! Please Wait...\n")

    for i in range(1, Repeat + 1, 1): #Iterating the same simulation multiple times

        print("Current Iteration: {} / {}" .format(i, Repeat), end = "\r")

        N_Arr = [Starting_N] #Collects the resulting N each time

        D_Arr =  [0] #Collects the resuling D for each Iteration

        for j in range(1, Period + 1, 1):

            N = N_Arr[j - 1] #Sets the starting population for calculation

            D = 0 #Collects the Delta each Period

            for k in range(1, N + 1, 1):

                br = random.binomial(1, b, 1)[0]

                dr = random.binomial(1, d + (c * N), 1)[0]

                if (br == 1):

                    D += 1

                if (dr == 1):

                    D -= 1

            N += D
            
            D_Arr.append(D) #Updating with the new values

            N_Arr.append(N) #Updating with the new values
        
        ax1.plot(Period_Arr, N_Arr, linestyle = ":")

        ax2.plot(Period_Arr, D_Arr, linestyle = ":")

        N_Tab.loc[i] = N_Arr
        
        D_Tab.loc[i] = D_Arr

    Avg_N = compute_mean(N_Tab, Period, Starting_N)

    Avg_D = compute_mean(D_Tab, Period, 0)

    N_Arr = compute_unique_Tab_Values(N_Tab, Period, Repeat)

    # Plot Average Simulation Results

    ax1.plot(Period_Arr, Avg_N, linewidth = 3, color = "k", label = "Average Population Growth")

    ax2.plot(Period_Arr, Avg_D, linewidth = 3, color = "k", label = "Average Delta Population")
    
    # Plot Theoretical Population Growth

    yn = [Starting_N]

    for j in range(1, Period + 1, 1):

        yn.append(yn[j - 1] + yn[j - 1] * (b - d - c * yn[j - 1]))

    ax1.plot(Period_Arr, yn, linewidth = 2, color = "m",  label = "Expected Population Growth")

    ax1.legend(loc = "upper left", fontsize = 6)
    
    # Plot Theoretical Delta Population Function

    yd = [0]

    for j in range(1, Period + 1, 1):

        yd.append(yn[j] - yn[j - 1])

    ax2.plot(Period_Arr, yd, linewidth = 2, color = "m", label = "Expected Delta Population")

    ax2.legend(loc = "upper left", fontsize = 6)

    # Plot Average Delta in function of the Population
    
    if (Compute_Avg_Delta_Population == True): 

        # Plot Actual Average Delta in function of Population

        Avg_D_N = compute_avg_Delta_Population(N_Arr, N_Tab, D_Tab, Period, Repeat)
        
        ax3 = fig.add_subplot(gs[:, 1])
        ax3.set_title("Delta in Function of Population")
        ax3.set_xlabel("Population") 
        ax3.set_ylabel("Delta", rotation = -90)
        ax3.yaxis.set_label_coords(1.05, 0.5) #Moving Y label for readability
        ax3.set_xlim(Starting_N, len(Avg_D_N) + 1)
        
        ax3.plot(Avg_D_N, color = "k", label = "Average Delta in function of Population")
   
        # Plot Theoretical Average Delta in function of Population

        xdn = linspace(0, len(Avg_D_N) + 1, 1000)

        ydn = xdn * (b - d - c * xdn)

        ax3.plot(xdn, ydn, linewidth = 2, color = "m", label = "Expected Delta in function of Population")
        
        ax3.legend(loc = "upper left", fontsize = 6)

    # Results Presentation

    print("\n\n\nInitial Population: ", Starting_N)
    print("\nLength of Period set: ", Period)
    print("\nBirth Rate set: ", b)
    print("\nDeath Rate set: ", d)
    print("\nCrowding Coefficient set: ", c)
    print("\nNumber of Iterations done: ", Repeat)

    print("\n\nAverage Final Population: ", Avg_N[Period])
    print("\nTheoretical Final Population: ", yn[Period])

    print("\n\nAverage Population per Period: \n")
    print(tabulate(DataFrame({"Period": Period_Arr, "Average Population": Avg_N, "Average Delta": Avg_D}), headers = ["Period", "Average Population", "Average Delta"], tablefmt = "github", numalign = "center", showindex = False))

    pyplot.show()

    print("\n\nSimulation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()