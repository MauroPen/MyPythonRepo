import os

def run_Birthday_Paradox():
    os.system('python MyPythonRepo/src/Birthday_Paradox/Birthday_Paradox.py')

def run_Collatz_Conjecture():
    os.system('python MyPythonRepo/src/Collatz_Conjecture/Collatz_Conjecture.py')

def run_program3():
    os.system('python program3/main_program3.py')

def run_program4():
    os.system('python program4/main_program4.py')

def main_menu():

    print("\nWelcome to MyPythonRepo!\n\nPlease choose an option from the Main Menu below.\n")

    while True:

        print("Main Menu\n")

        print("1. Run Birthday Paradox\n")

        print("2. Run Collatz Conjecture\n")

        print("5. Exit\n")

        choice = int(input("Select an option: \n"))

        match choice:

            case 1:

                run_Birthday_Paradox()

            case 2:

                run_Collatz_Conjecture()

            case 5:

                print("\nExiting...\n")
                break
        
            case _:

                print("\nYour selection is not valid, please enter a valid number.\n")


if __name__ == "__main__":

    main_menu()