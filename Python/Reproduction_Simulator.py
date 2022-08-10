# Reproduction Simulator

from numpy import random
from tabulate import tabulate
from matplotlib import pyplot

print("Welcome to the Reproduction Simulator!\n")

# Variables settings

N = int(input("\nPlease input the Inital Number of Population (Initial_Population) that you want to set:\n", )) # Exceptions to be added

Period = int(input("\nAmazing! Now, please input the length of the Period of time that you want to consider for the simulation:\n"))

b = float(input("\nGreat! Now, please input the Birth Rate (Birth_Rate):\n", )) # Exceptions to be added

d = float(input("\nFinally, please input the desired Death Rate (Death_Rate): \n", )) # Exceptions to be added

# Computation

Period_Tab = list(range(0, Period + 1, 1)) #Indexes the periods, necessary for plots

N_Tab = [N] #Collects the resulting N each time

D_Tab =  [0]#Collects the resuling D each time

for i in range(1, Period + 1, 1):

    D = 0 #Collects the Delta each time

    for j in range(1, N + 1, 1):

        br = random.binomial(1, b, 1)[0]

        dr = random.binomial(1, d, 1)[0]

        if (br == 1):

            D += 1

        elif (dr == 1):

            D -= 1

        # print("\nProcessing! Please Wait...\n\nCurrent Person Evaluated: ", j, "/", N)

    D_Tab.append(D)
    
    N += D

    N_Tab.append(N)

# print("\nProcessing! Please Wait...\n\nCurrent Day: ", i, "/", Period)

# Results Presentation

print("\n", tabulate(list(zip(N_Tab, D_Tab)), headers = ["Period", "Population", "Delta"], showindex = True, tablefmt = "github", numalign = "center"))

print("\nInitial_Population: ", N_Tab[0])
print("\nBirth Rate set: ", b)
print("\nDeath Rate set: ", d)
print("\nFinal_Population: ", N_Tab[Period])
print("\nTotal_Delta: ", sum(D_Tab))

pyplot.title("Simulation Results") 
pyplot.xlabel("Period") 
pyplot.ylabel("Population") 
pyplot.plot(Period_Tab, N_Tab)
pyplot.show()