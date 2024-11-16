import subprocess

from Dependency_Manager import check_modules

def run_Birthday_Paradox():
    
    print ("\nChecking dependencies to run Birthday Paradox...")

    modules = ["numpy", "pandas", "datetime", "math", "tabulate"]
    check_modules(modules)

    subprocess.run(["python", f"src/Birthday_Paradox/Birthday_Paradox.py"])

def run_Collatz_Conjecture():
    
    print ("\nChecking dependencies to run Collatz Conjecture...")

    modules = ["numpy", "pandas", "IPython", "matplotlib", "datetime", "tabulate"]
    check_modules(modules)
    
    subprocess.run(["python", f"src/Collatz_Conjecture/Collatz_Conjecture.py"])

def run_Reproduction_Simulator():
    
    print ("\nChecking dependencies to run Reproduction Simulator...")

    modules = ["numpy", "pandas", "matplotlib", "datetime", "tabulate", "math"]
    check_modules(modules)
    
    subprocess.run(["python", f"src/Reproduction_Simulator/Reproduction_Simulator.py"])

def run_Check_Numbers_Pi():
    
    print ("\nChecking dependencies to run Check Numbers Pi...")

    modules = ["math_pi"]
    check_modules(modules)
    
    subprocess.run(["python", f"src/Check_Numbers_Pi/Check_Numbers_Pi.py"])

def run_Fibonacci():
    
    subprocess.run(["python", f"src/Fibonacci_Series/Fibonacci_Series.py"])

def main_menu():

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

                run_Birthday_Paradox()

            case 2:

                run_Collatz_Conjecture()

            case 3:

                run_Reproduction_Simulator()

            case 4:

                run_Check_Numbers_Pi()

            case 5:

                run_Fibonacci()

            case 6:

                print("\nExiting...\n")

                break
        
            case _:

                print("\nYour selection is not valid, please enter a valid number.\n")


if __name__ == "__main__":

    main_menu()