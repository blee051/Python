#This is Brandon's Lab 5b Assignment
#Lab 5b Fahrenheit to Celsius converter
#Name: Brandon Lee
#Version: 3
#Date 6-14-23

#Libraries
import sys

#Global Constants
YES = "yes"
NO = "no"
EXIT = 'x'
OPTION_ONE = '1'
OPTION_TWO = '2'
THIRTYTWO = 32
ONEPOINTEIGHT = 1.8
FIVEDIVNINE = 0.55556

#Celsius to Fahrenheit function
def celsius_to_fahrenheit(cDegrees):
    return (cDegrees*ONEPOINTEIGHT)+ THIRTYTWO

#Fahrenheit to Celsius function
def fahrenheit_to_celsius(fDegrees):
    return (fDegrees - THIRTYTWO)*FIVEDIVNINE

#Header function
def header():
    print("Welcome, this is a Fahrenheit to Celsius converter.\n")

#Option select function
def option_select():
    counter = 4
    while counter != 0:
        counter -= 1
        if counter == 0:
            print("Max tries made. End of program")
            sys.exit()
        print("Selection Screen!!!")
        print("1 = Celsius to Fahrenheit converter.")
        print("2 = Fahrenheit to Celsius converter.")
        print("x = Exit")
        inVal = input("Option: ")
        if inVal == OPTION_ONE:
            print("\nGood. You have chosen Celsius to Fahrenheit converter.")
            return '1'
        elif inVal == OPTION_TWO:
            print("\nGood. You have chosen Fahrenheit to Celsius converter.")
            return '2'
        elif inVal == EXIT:
            print("\nExit Program")
            sys.exit()
        else:
            print("You have not selected a correct input. You have", end=" ")
            print(counter, "tries left. Please try again")

#Converter Function
def converter(option):
    if option == OPTION_ONE:
        inputVal = input("Enter your Celsius temperature value: ")
        outputVal = celsius_to_fahrenheit(float(inputVal))
        print("\nYou have selected,", inputVal, "Degrees Celsius.")
        print("Calculation:",inputVal, "*1.8+32 =", outputVal)
        print("The convertion is:", outputVal, "Degrees Fahrenheit.\n")
    else: #option 2
        inputVal = input("Enter your Fahrenheit value: ")
        outputVal = fahrenheit_to_celsius(float(inputVal))
        print("\nYou have selected,", inputVal, "Degrees Fahrenheit.")
        print("Calculation: ("+str(inputVal)+ "-32)*5/9=", outputVal)
        print("The convertion is:", outputVal, "Degrees Celsius.\n")

#Want to do it again? function
def again():
    counter = 4
    while counter != 0:
        counter -= 1
        if counter == 0:
            print("Max tries reached")
            return
        inputVal = input("Do you want to convert again? (yes/no).").lower()
        if inputVal == YES:
            main()
            return
        elif inputVal == NO:
            return
        else:
            print("Incorrect option. You have", counter, "tries left.")

#Closer function
def closer():
    print("End of program. Goodbye.")
    sys.exit()

#Main Function
def main():
    header()
    converter(option_select())
    again()
    closer()


main()
#PROFESSOR - PLEASE READ
#This will be posted to my github. Please provide any feedback on how I can improve my code.
#Please introduce any concepts not mentioned in class, if possible. It would be of great resource.
#What would a employer want from my code? Is my code readable?
#Thank you.
