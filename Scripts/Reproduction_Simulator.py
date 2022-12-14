# Reproduction Simulator

from math import isnan
from IPython.display import display
from numpy import random, mean, linspace, full, unique
from matplotlib import pyplot, gridspec
from pandas import DataFrame, Series, option_context, ExcelWriter
from tabulate import tabulate
from os import getcwd
from datetime import datetime
from sys import warnoptions

if not warnoptions:

    from warnings import simplefilter

    simplefilter("ignore")


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


def float_input_check():

    float_input = -1.0

    while (float_input < 0):

        try:

            float_input = float(input())

            while (not(float_input >= 0 and float_input <= 1)):

                print("\nThe inserted value is not valid, please input a number between 0 and 1:\n")

                float_input = float(input())

            return float_input

        except:

            print("\nThe inserted value is not valid, please input a number between 0 and 1:\n")

            float_input = -1
    

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

    print("\n\nAlmost done! Please, wait while computing the Average Delta in function of the Population...\n")

    for i in range(0, int(max(Unique_Array)) + 1, 1):

        print("Current Iteration: {Iteration} / {Total_Iterations}" .format(Iteration = i, Total_Iterations = int(max(Unique_Array))), end = "\r")

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

    # Export Results in .csv Files? (y/n)
    
    print("\n\nDo you want to export the results of the simulation? (y/n)\n\nWARNING! This will create one or more new files in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = getcwd()))
    
    if (yn_input_check() == True):

        print("\n\nDo you want to export the results in a single .xlsx file (1), in three separated .csv files (2), or both (3)? If you changed your mind, just enter \"4\"\n")

        Export_File = int_input_check()
        
        while (Export_File < 1 or Export_File > 4):
        
            print("\nThe inserted value is not valid, please input a number between 1 and 4:\n")

            Export_File = int_input_check()

    else:

        Export_File = 0

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

        print("Current Iteration: {Iteration} / {Total_Iterations}" .format(Iteration = i, Total_Iterations = Repeat), end = "\r")

        N_Arr = [Starting_N] #Collects the resulting N each time

        D_Arr =  [0] #Collects the resuling D for each Iteration

        for j in range(1, Period + 1, 1):

            N = N_Arr[j - 1] #Sets the starting population for calculation

            D = 0 #Collects the Delta each Period

            for k in range(1, N + 1, 1):

                br = random.binomial(1, b, 1)[0]

                if (br == 1):

                    D += 1
                
                if (d + (c * N) <= 1):
                    
                    dr = random.binomial(1, d + (c * N), 1)[0]

                    if (dr == 1):

                        D -= 1

                else:

                    D-= 1

            N += D
            
            D_Arr.append(D) #Updating with the new values

            N_Arr.append(N) #Updating with the new values
        
        ax1.plot(Period_Arr, N_Arr, linestyle = ":")

        ax2.plot(Period_Arr, D_Arr, linestyle = ":")

        N_Tab.loc[i] = N_Arr
        
        D_Tab.loc[i] = D_Arr

    Avg_N = compute_mean(N_Tab, Period, Starting_N)

    Avg_D = compute_mean(D_Tab, Period, 0)

    Avg_Tab = DataFrame({"Period": Period_Arr, "Average Population": Avg_N, "Average Delta": Avg_D}, index = list(range(0, Period + 1, 1)))

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
        
        N_Array = compute_unique_Tab_Values(N_Tab, Period, Repeat)

        Avg_D_N = compute_avg_Delta_Population(N_Array, N_Tab, D_Tab, Period, Repeat)
        
        ax3 = fig.add_subplot(gs[:, 1])
        ax3.set_title("Delta in Function of Population")
        ax3.set_xlabel("Population") 
        ax3.set_ylabel("Delta", rotation = -90)
        ax3.yaxis.set_label_coords(1.05, 0.5) #Moving Y label for readability
        ax3.set_xlim(min(N_Array), len(Avg_D_N) + 1)
        
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
    print("\nTheoretical Final Population: ", "{:.2f}" .format(yn[Period]))

    with option_context("display.max_rows", None,
                        "display.max_columns", 10,
                        "display.width", 1000,
                        "display.colheader_justify", "center",
                        "display.precision", 2): #Sets options of visualization for display() valid only for the "with" instance

        print("\n\nResults of the simulation:")

        print("\nPopulation: per Period:\n")
        
        display(N_Tab)

        print("\nDelta Population: per Period:\n")
        
        display(D_Tab)
        
        print("\n\nAverage Population per Period: \n")
        
        print(tabulate(Avg_Tab, headers = Avg_Tab.columns, tablefmt = "github", numalign = "center", showindex = "False"))
    
    # Export Results

    datetime_string = datetime.now().strftime("%d_%m_%Y - %H_%M_%S")

    if (Export_File == 1 or Export_File == 3):

        # Export the values obtained in a single .xlsx file

        with ExcelWriter ("Simulation Results ({Timestamp}).xlsx" .format(Timestamp = datetime_string)) as writer:

            N_Tab.to_excel(writer, sheet_name = "Population Overtime", index = True)
            
            D_Tab.to_excel(writer, sheet_name = "Delta Population Overtime", index = True)

            Avg_Tab.to_excel(writer, sheet_name = "Average Delta Population", index = False)

            print("\nIn this directory: {Current_Working_Directory}\nA file named: \"Simulation Results ({Timestamp}).xlsx\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), Timestamp = datetime_string))

    if (Export_File == 2 or Export_File == 3):
        
        # Export the values obtained in three different .csv files

        N_Tab.to_csv("Population_Overtime ({Timestamp}).csv" .format(Timestamp = datetime_string), index = True)

        print("\nIn this directory: {Current_Working_Directory}\nA file named: \"Population_Overtime ({Timestamp}).csv\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), Timestamp = datetime_string))

        D_Tab.to_csv("Delta_Population_Overtime ({Timestamp}).csv" .format(Timestamp = datetime_string), index = True)

        print("\nIn this directory: {Current_Working_Directory}\nA file named: \"Delta_Population_Overtime ({Timestamp}).csv\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), Timestamp = datetime_string))

        Avg_Tab.to_csv("Average_Delta_Population ({Timestamp}).csv" .format(Timestamp = datetime_string), index = False)

        print("\nIn this directory: {Current_Working_Directory}\nA file named: \"Average_Delta_Population ({Timestamp}).csv\" has been successfully created!\n" .format(Current_Working_Directory = getcwd(), Timestamp = datetime_string))

    pyplot.show()

    print("\nSimulation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()