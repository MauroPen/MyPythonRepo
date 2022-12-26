from math import isnan
from numpy import array, concatenate, random, mean, linspace, full, unique, append
from matplotlib import pyplot, gridspec
from pandas import DataFrame, RangeIndex
from tabulate import tabulate
from os import getcwd
from datetime import datetime

from Common import yn_input_check, int_input_check, probability_input_check, DataframeExport, export_dataframes


def compute_mean_Arr(Array, Repeat, Period, Starting_Value):

    Avg_Array = [Starting_Value * Repeat]

    for i in range(1, Period + 1, 1):

        Avg_Array.append(0)

        for j in range(1, Repeat + 1, 1):

            Avg_Array[i] += Array[j][i]

    Avg_Array[:] = [value / Repeat for value in Avg_Array]

    return Avg_Array


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


def compute_Avg_Delta_Population(Unique_N, N_Array, D_Array, Period, Repeat):

    Avg_Values = []

    print("\n\nAlmost done! Please, wait while computing the Average Delta in function of the Population...\n")

    for N in range(int(min(Unique_N)), int(max(Unique_N)) + 1, 1):

        print("Current Iteration: {Iteration} / {Total_Iterations}" .format(Iteration = N, Total_Iterations = int(max(Unique_N))), end = "\r")

        collector = [] #Collects the values of D to average for each N

        for j in range(0, Period, 1): # Only "Period" because there is no data available for the last Period of simulation

            for k in range(1, Repeat + 1, 1):
            
                if (N_Array[k][j] == N):
                    
                    collector.append(D_Array[k][j + 1])
            
        if (isnan(mean(collector)) == True):

            Avg_Values.append(0)

        else:

            Avg_Values.append(mean(collector))

    return Avg_Values


#Setting Default Values

running = bool(True)

default_Starting_N = int(25)

default_Period = int(100)

default_b = float(0.2)

default_d = float(0.1)

default_c = float(0.001)

default_Repeat = int(200)

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
        
        b = probability_input_check()

        print("\nAwesome! Now, please input the desired Death Rate:\n")

        d = probability_input_check()

        print("\n\nFantastic! Now, please input the Crowding Coefficient. \n\nWARNING! This coefficient will positively affect the Death Rate of your population for each period (recommended value: 0.001):\n")

        c = probability_input_check()

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

    timeExecutionStart = datetime.now()

    Period_Arr = tuple(range(0, Period + 1, 1))  #Indexes the periods, necessary for plots

    N_Array = array([full(Period + 1, 0)])       #Collects the values taken by N from the different simulations, first one is a dummy 

    D_Array = array([full(Period + 1, 0)])       #Collects the values taken by D from the different simulations, first one is a dummy 

    # Plot Simulation Results

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

    timeSimulationStart = datetime.now()

    for iteration in range(1, Repeat + 1, 1): #Iterating the same simulation multiple times

        print("Current Iteration: {Iteration} / {Total_Iterations}" .format(Iteration = iteration, Total_Iterations = Repeat), end = "\r")

        N_Arr = [Starting_N]                  #Collects the resulting N each time

        D_Arr =  [0]                          #Collects the resuling D for each Iteration

        for period in range(1, Period + 1, 1):

            N = N_Arr[period - 1]             #Sets the starting population for calculation

            D = 0                             #Collects the Delta each Period

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
            
            D_Arr.append(D)                 #Updating with the new values

            N_Arr.append(N)                 #Updating with the new values
        
        ax1.plot(Period_Arr, N_Arr, linestyle = ":")

        ax2.plot(Period_Arr, D_Arr, linestyle = ":")
        
        N_Array = concatenate((N_Array, array([N_Arr])))

        D_Array = concatenate((D_Array, array([D_Arr])))

    Avg_N_Array = compute_mean_Arr(N_Array, Repeat, Period, Starting_N)

    Avg_D_Array = compute_mean_Arr(D_Array, Repeat, Period, 0)

    timeSimulationEnd = datetime.now()

    timeSimulation = (timeSimulationEnd - timeSimulationStart)

    # Plot Average Simulation Results

    timePlottingStart = datetime.now()

    ax1.plot(Period_Arr, Avg_N_Array, linewidth = 3, color = "k", label = "Average Population Growth")

    ax2.plot(Period_Arr, Avg_D_Array, linewidth = 3, color = "k", label = "Average Delta Population")
    
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

    (timePlottingEnd, timeExecutionEnd) = (datetime.now(), datetime.now())

    timePlotting = (timePlottingEnd - timePlottingStart)

    timeExecution = (timeExecutionEnd - timeExecutionStart)

    # Results Presentation

    print("\n\n\nInitial Population: ", Starting_N)
    print("\nLength of Period set: ", Period)
    print("\nBirth Rate set: ", b)
    print("\nDeath Rate set: ", d)
    print("\nCrowding Coefficient set: ", c)
    print("\nNumber of Iterations done: ", Repeat)

    print("\n\nAverage Final Population: ", Avg_N_Array[Period])
    print("\nTheoretical Final Population: ", "{:.2f}" .format(yn[Period]))

    timesTable = [["Total time for running simulations", str(timeSimulation)],
                  ["Total time spent plotting", str(timePlotting)],
                  ["Total time of execution", str(timeExecution)]]
        
    print("\n")

    print(tabulate(timesTable, headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))

    pyplot.show()
    
    # Export Results
    
    print("\n\nDo you want to export the results of the simulation? (y/n)\n\nWARNING! This will create a new file in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = getcwd()))
    
    if (yn_input_check() == True):

        timeExportStart = datetime.now()

        Columns_Period_Arr = []
        
        for period in Period_Arr:

            Columns_Period_Arr = append(Columns_Period_Arr, "Period {number}" .format(number = period))

        N_Tab = DataFrame(N_Array[1:], columns = Columns_Period_Arr, index = RangeIndex(1, Repeat + 1, 1))
        
        D_Tab = DataFrame(D_Array[1:], columns = Columns_Period_Arr, index = RangeIndex(1, Repeat + 1, 1))

        Avg_D_N_Tab = DataFrame({"Average Population": Avg_N_Array, "Average Delta": Avg_D_Array}, index = RangeIndex(0, Period + 1, 1))

        dataframes = [DataframeExport(N_Tab, "Population Overtime", True), DataframeExport(D_Tab, "Delta Population Overtime", True), DataframeExport(Avg_D_N_Tab, "Average Values Overtime", True)]

        export_dataframes(dataframes, fileName = "Reproduction Simulator Results")

        timeExportEnd = datetime.now()

        timeExport = (timeExportEnd - timeExportStart)

        print(tabulate([["Time spent exporting data", str(timeExport)]], headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))
    
    # Computation of Average Delta in function of the Population? (y/n) TO BE REFACTORED
    
    print("\n\nDo you want to compute the Average Delta in function of the Population too? (y/n)\n\nWARNING! This computation may require longer times of execution of the program.\n")

    Compute_Avg_Delta_Population = yn_input_check()
    
    if (Compute_Avg_Delta_Population == True):

        timeAverageDeltaPopulationStart = datetime.now()

        # Plot Actual Average Delta in function of Population

        gs = gridspec.GridSpec(1, 1)

        fig = pyplot.figure()

        Unique_N = unique(N_Array)

        Avg_D_N_Array = compute_Avg_Delta_Population(Unique_N, N_Array, D_Array, Period, Repeat)
        
        ax3 = fig.add_subplot(gs[0, 0])
        ax3.set_title("Delta in Function of Population")
        ax3.set_xlabel("Population") 
        ax3.set_ylabel("Delta", rotation = -90)
        ax3.yaxis.set_label_coords(1.05, 0.5) #Moving Y label for readability
        ax3.set_xlim(Unique_N[1], len(Avg_D_N_Array) + 1)
        
        ax3.plot(Avg_D_N_Array, color = "k", label = "Average Delta in function of Population")
   
        # Plot Theoretical Average Delta in function of Population

        xdn = linspace(min(Unique_N), max(Unique_N), 1000)

        ydn = xdn * (b - d - c * xdn)

        ax3.plot(xdn, ydn, linewidth = 2, color = "m", label = "Expected Delta in function of Population")
        
        ax3.legend(loc = "upper left", fontsize = 6)

        timeAverageDeltaPopulationEnd = datetime.now()

        timeAverageDeltaPopulation = (timeAverageDeltaPopulationEnd - timeAverageDeltaPopulationStart)

        print(tabulate([["Time spent computing the Average Delta in function of Population", str(timeAverageDeltaPopulation)]], headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))

        pyplot.show()

    print("\nSimulation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()