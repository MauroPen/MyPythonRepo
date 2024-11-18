import os
import subprocess

from dependency_manager import retrieve_modules, check_modules

def run_Birthday_Paradox(baseDir):
    
    print ("\nChecking dependencies to run Birthday Paradox...")

    modules = retrieve_modules(baseDir, "Birthday Paradox")

    check_modules(modules)

    birthdayParadoxPath = os.path.join(baseDir, "Birthday_Paradox", "Birthday_Paradox.py")
    
    subprocess.run(["python", birthdayParadoxPath])

def run_Collatz_Conjecture(baseDir):
    
    print ("\nChecking dependencies to run Collatz Conjecture...")

    modules = retrieve_modules(baseDir, "Collatz Conjecture")

    check_modules(modules)
    
    collatzConjecturePath = os.path.join(baseDir, "Collatz_Conjecture", "Collatz_Conjecture.py")
    
    subprocess.run(["python", collatzConjecturePath])

def run_Reproduction_Simulator(baseDir):
    
    print ("\nChecking dependencies to run Reproduction Simulator...")

    modules = retrieve_modules(baseDir, "Reproduction Simulator")

    check_modules(modules)
    
    reproductionSimulatorPath = os.path.join(baseDir, "Reproduction_Simulator", "Reproduction_Simulator.py")
    
    subprocess.run(["python", reproductionSimulatorPath])

def run_Check_Numbers_Pi(baseDir):
    
    print ("\nChecking dependencies to run Check Numbers Pi...")

    modules = retrieve_modules(baseDir, "Check Numbers Pi")

    check_modules(modules)
    
    checkNumbersPiPath = os.path.join(baseDir, "Check_Numbers_Pi", "Check_Numbers_Pi.py")
    
    subprocess.run(["python", checkNumbersPiPath])

def run_Fibonacci_Series(baseDir):
    
    print ("\nChecking dependencies to run Fibonacci Series...")

    modules = retrieve_modules(baseDir, "Fibonacci Series")

    check_modules(modules)
    
    fibonacciSeriesPath = os.path.join(baseDir, 'Fibonacci_Series', 'Fibonacci_Series.py')
    
    subprocess.run(["python", fibonacciSeriesPath])

def main_menu():

    baseDir = os.path.dirname(os.path.abspath(__file__))       #Gets the current directory from main.py
    
    print("\nWelcome to MyPythonRepo!\n\nPlease choose an option from the Main Menu below.\n")

    while True:

        print("Main Menu\n")

        print("1. Run Birthday Paradox\n")

        print("2. Run Collatz Conjecture\n")

        print("3. Run Reproduction Simulator\n")

        print("4. Run Check Numbers Pi\n")

        print("5. Run Fibonacci Series\n")

        print("6. Exit\n")

        choice = int(input("Select an option: \n"))

        match choice:

            case 1:

                run_Birthday_Paradox(baseDir)

            case 2:

                run_Collatz_Conjecture(baseDir)

            case 3:

                run_Reproduction_Simulator(baseDir)

            case 4:

                run_Check_Numbers_Pi(baseDir)

            case 5:

                run_Fibonacci_Series(baseDir)

            case 6:

                print("\nExiting...\n")

                break
        
            case _:

                print("\nYour selection is not valid, please enter a valid number.\n")


if __name__ == "__main__":

    main_menu()