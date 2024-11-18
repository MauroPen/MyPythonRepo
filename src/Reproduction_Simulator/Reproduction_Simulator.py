import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from numpy import array, concatenate, mean, linspace, full, unique, append
from pandas import DataFrame, RangeIndex
from matplotlib import pyplot, gridspec
from datetime import datetime, timedelta
from tabulate import tabulate

from shared.common import yn_input_check, int_input_check, probability_input_check, DataframeExport, export_dataframes

from Reproduction_Simulator.dependency import main_computation, compute_mean, compute_avg_delta_population


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

        print("\nPlease input the Inital Population that you want to set (for reference, default value is 25):\n")
        
        Starting_N = int_input_check()

        print("\nAmazing! Now, please input the length of the Period of time that you want to consider for the simulation (for reference, default value is 100):\n")
        
        Period = int_input_check()

        print("\nGreat! Now, please input the Birth Rate (for reference, default value is 0,2):\n")
        
        b = probability_input_check()

        print("\nAwesome! Now, please input the desired Death Rate (for reference, default value is 0,1):\n")

        d = probability_input_check()

        print("\n\nFantastic! Now, please input the Crowding Coefficient. \n\nWARNING! This coefficient will positively affect the Death Rate of your population for each period (recommended value: 0.001):\n")

        c = probability_input_check()

        print("\nFinally, please input the number of times that you want this simulation to be repeated (for reference, default value is 200):\n")

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

    print("\nDo you want to compute the Average Delta in function of the Population too? (y/n)\n\nWARNING! This computation may require longer times of execution of the program.\n")

    Compute_avg_delta_population = yn_input_check()

    # Computation

    timeSimulation = timedelta(seconds = 0)

    timeAverageDeltaPopulation = timedelta(seconds = 0)
    
    timeExecution = timedelta(seconds = 0)

    timeExecutionStart = datetime.now()

    Period_Arr = tuple(range(0, Period + 1, 1))  #Indexes the periods, necessary for plots

    N_Array = array([full(Period + 1, 0)])       #Collects the values taken by N from the different simulations, first one is a dummy 

    D_Array = array([full(Period + 1, 0)])       #Collects the values taken by D from the different simulations, first one is a dummy 

    # Plot Simulation Results

    if (Compute_avg_delta_population == True):

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

    timeSimulationStart = datetime.now()

    for iteration in range(1, Repeat + 1, 1): #Iterating the same simulation multiple times

        print("Current Iteration: {Iteration} / {Total_Iterations}" .format(Iteration = iteration, Total_Iterations = Repeat), end = "\r")

        (N_Arr, D_Arr) = main_computation(Starting_N, Period, b, d, c)
        
        ax1.plot(Period_Arr, N_Arr, linestyle = ":")

        ax2.plot(Period_Arr, D_Arr, linestyle = ":")
        
        N_Array = concatenate((N_Array, array([N_Arr])))

        D_Array = concatenate((D_Array, array([D_Arr])))

    Avg_N_Array = compute_mean(N_Array, Repeat, Period, Starting_N)

    Avg_D_Array = compute_mean(D_Array, Repeat, Period, 0)

    timeSimulationEnd = datetime.now()

    timeSimulation = (timeSimulationEnd - timeSimulationStart)

    # Plot Average Simulation Results

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
        
    # Computation of Average Delta in function of the Population
    
    if (Compute_avg_delta_population == True):

        timeAverageDeltaPopulationStart = datetime.now()

        Unique_N = unique(N_Array)

        Avg_D_N_Array = compute_avg_delta_population(Unique_N, N_Array, D_Array, Period, Repeat)

        timeAverageDeltaPopulationEnd = datetime.now()

        timeAverageDeltaPopulation = (timeAverageDeltaPopulationEnd - timeAverageDeltaPopulationStart)
        
        # Plot Actual Average Delta in function of Population

        ax3 = fig.add_subplot(gs[:, 1])
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

    timeExecutionEnd = datetime.now()

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
                  ["Time spent computing the Average Delta in function of Population", str(timeAverageDeltaPopulation)],
                  ["Total time of execution", str(timeExecution)]]
        
    print("\n")

    print(tabulate(timesTable, headers = ["Phase", "Duration"], tablefmt = "github", stralign = "center", showindex = "False"))

    pyplot.show()

    # Export Results
    
    print("\n\nDo you want to export the results of the simulation? (y/n)\n\nWARNING! This will create a new file in your current working directory, which is: {Current_Working_Directory}\n" .format(Current_Working_Directory = os.getcwd()))
    
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

    print("\nSimulation ended!\n\nDo you want to start over? (y/n)\n")
    
    running = yn_input_check()