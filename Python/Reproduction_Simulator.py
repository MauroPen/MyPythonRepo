# Reproduction Simulator

from numpy import random

print("Welcome to the Reproduction Simulator!\n")

# Variables settings

N = int(input("\nPlease input the Inital Number of Population (Initial_Population) that you want to set:\n", )) # Exceptions to be added

b = float(input("\nGreat! Now, please input the Birth Rate (Birth_Rate):\n", )) # Exceptions to be added

d = float(input("\nFinally, please input the desired Death Rate (Death_Rate): \n", )) # Exceptions to be added

# Computation

Days = 10 #Must become a parameter set by the user

N_Tab = [N] #Collects the resulting N each time

D_Tab =  [0]#Collects the resuling D each time

for i in range(1, Days + 1, 1):

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

# print("\nProcessing! Please Wait...\n\nCurrent Day: ", i, "/", Days)

# Results Presentation

print("\nInitial_Population: ", N_Tab[0])
print("\nFinal_Population: ", N_Tab[Days - 1])

print("\nTotal Delta: ", sum(D_Tab))

print("\n",N_Tab, "\n",D_Tab)







