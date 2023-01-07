from numpy import random, append, mean
from math import isnan
from sys import warnoptions     #Necessary to avoid some annoying warnings about "mean"

if not warnoptions: 

    from warnings import simplefilter

    simplefilter("ignore")


#1 - Main computation algorythm
def main_computation(Starting_N, Period, b, d, c):

    N_Arr = [Starting_N]                  #Collects the resulting N after each Period

    D_Arr =  [0]                          #Collects the resulting D after each Period

    for period in range(1, Period + 1, 1):

        N = N_Arr[period - 1]             #Sets the starting population for calculation

        D = 0                             #Collects the Delta each Period

        for person in range(1, N + 1, 1):

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

    return (N_Arr, D_Arr)

#2 - Computes the average Population per period for each simulation
def compute_mean(Array, Repeat, Period, Starting_Value):

    Avg_Array = [Starting_Value * Repeat]

    for i in range(1, Period + 1, 1):

        Avg_Array.append(0)

        for j in range(1, Repeat + 1, 1):

            Avg_Array[i] += Array[j][i]

    Avg_Array[:] = [value / Repeat for value in Avg_Array]

    return Avg_Array

#3 - Computes the average Delta in function of the Population
def compute_avg_delta_population(Unique_N, N_Array, D_Array, Period, Repeat):

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
