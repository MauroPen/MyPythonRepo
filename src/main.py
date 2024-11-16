import os
import subprocess

from Dependency_Manager import check_modules

def run_Birthday_Paradox(base_dir):
    
    print ("\nChecking dependencies to run Birthday Paradox...")

    modules = ["numpy", "pandas", "math", "tabulate"]
    check_modules(modules)

    birthdayParadoxPath = os.path.join(base_dir, "Birthday_Paradox", "Birthday_Paradox.py")
    
    subprocess.run(["python", birthdayParadoxPath])

def run_Collatz_Conjecture(base_dir):
    
    print ("\nChecking dependencies to run Collatz Conjecture...")

    modules = ["numpy", "pandas", "IPython", "matplotlib", "tabulate"]
    check_modules(modules)
    
    collatzConjecturePath = os.path.join(base_dir, "Collatz_Conjecture", "Collatz_Conjecture.py")
    
    subprocess.run(["python", collatzConjecturePath])

def run_Reproduction_Simulator(base_dir):
    
    print ("\nChecking dependencies to run Reproduction Simulator...")

    modules = ["numpy", "pandas", "matplotlib", "tabulate", "math"]
    check_modules(modules)
    
    reproductionSimulatorPath = os.path.join(base_dir, "Reproduction_Simulator", "Reproduction_Simulator.py")
    
    subprocess.run(["python", reproductionSimulatorPath])

def run_Check_Numbers_Pi(base_dir):
    
    print ("\nChecking dependencies to run Check Numbers Pi...")

    modules = ["pandas", "math_pi"]
    check_modules(modules)
    
    checkNumbersPiPath = os.path.join(base_dir, "Check_Numbers_Pi", "Check_Numbers_Pi.py")
    
    subprocess.run(["python", checkNumbersPiPath])

def run_Fibonacci_Series(base_dir):
    
    print ("\nChecking dependencies to run Fibonacci Series...")

    modules = ["pandas"]
    check_modules(modules)
    
    fibonacciSeriesPath = os.path.join(base_dir, 'Fibonacci_Series', 'Fibonacci_Series.py')
    
    subprocess.run(["python", fibonacciSeriesPath])

def main_menu():

    base_dir = os.path.dirname(os.path.abspath(__file__))       #Gets the current directory from main.py
    
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

                run_Birthday_Paradox(base_dir)

            case 2:

                run_Collatz_Conjecture(base_dir)

            case 3:

                run_Reproduction_Simulator(base_dir)

            case 4:

                run_Check_Numbers_Pi(base_dir)

            case 5:

                run_Fibonacci_Series(base_dir)

            case 6:

                print("\nExiting...\n")

                break
        
            case _:

                print("\nYour selection is not valid, please enter a valid number.\n")


if __name__ == "__main__":

    main_menu()