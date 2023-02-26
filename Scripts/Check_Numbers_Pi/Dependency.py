import math_pi
import re

#1 - Check user input
def number_check():

    char_input = "Default"

    while(not(re.match("^[0-9]+$", char_input))):
            
            char_input = input()

            if (not(re.match("^[0-9]+$", char_input))):

                print("\nThe inserted value is not valid, please input only numbers: ")
        
    return char_input

#2 - Retrieve pi --> To be improved
def retrieve_pi():
    
    return str(math_pi.pi(1, 1000000)).replace(".","")  # Converting pi into string and removing decimal point

#3 - Main computation (returning a dictionary)
def main_computation(digitsToBeFound):

    result = {
        "Digits Checked": 0,
        "Pi Until": "3.14",
        "Not Found": True
    }
    
    pi = retrieve_pi()

    digitsChecked = 0

    for piDigit in pi:

        if piDigit == digitsToBeFound[0]:

            piCompare = pi[digitsChecked:(digitsChecked + len(digitsToBeFound))]

            if piCompare == digitsToBeFound:

                result["Digits Checked"] = digitsChecked
                result["Pi Until"] = pi[:digitsChecked + len(digitsToBeFound)]
                result["Not Found"] = False

                return result

        digitsChecked += 1
    
    result["Digits Checked"] = digitsChecked
    result["Pi Until"] = pi
    
    return result