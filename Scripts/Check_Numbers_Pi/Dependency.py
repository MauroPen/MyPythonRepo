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

#3 - Main computation --> returning a dictionary
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

#4 - Number of occurrencies --> to be used after checking the combination with main_computation
def check_occurrencies(combination, digits_until):

    occurrencies = 1        #At least 1, the function is meant to be used after main_computation
    
    pi = retrieve_pi()

    digitsChecked = digits_until + len(combination)     #First occurrency is already included

    for piDigit in pi[(digitsChecked):]:

        if piDigit == combination[0]:

            piCompare = pi[digitsChecked:(digitsChecked + len(combination))]

            if piCompare == combination:

                occurrencies += 1

        digitsChecked += 1

    return occurrencies

#5 - Print the whole pi until combination --> deprecated to save it in a .txt file
def print_whole_pi_until(pi_until):

    temp_list = []

    temp_list[:0] = pi_until

    for digit in temp_list:

        print(digit, end = "")