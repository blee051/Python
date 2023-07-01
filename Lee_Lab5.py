#This is Brandon's Lab 5 Assignment
#Lab 5: Is it prime?
#Name: Brandon
#Date: 6-18-23

#Libraries
import sys

#Header
def header():
    print("Welcome to my Prime number checker.\n")

#Input function
def input_value():
    counter = 4
    while counter != 0:
        counter -= 1
        try:
            inValue = int(input())
            return inValue
        #Checking for error
        except ValueError:
            print("Error: Please input whole numbers")
            print("You have", counter,"tries left.")
        if counter == 0:
            print("Max tries reached. Ending Program")
            sys.exit()

#Asking user for range of numbers
def my_range():
    #Start
    print("Please enter the beginning number: ")
    start = input_value()
    #End
    print("Please enter the end number: ")
    end = input_value()

    numberList = list(range(start, end+1))
    print("Your range is:", numberList)
    return numberList

#Scanning list for all prime numbers
def find_prime(myList):
    primeNumbers = []
    for x in myList:
        if is_prime(x):
            primeNumbers.append(x)

    return primeNumbers

#Bool Function checking input for Pime number
def is_prime(inValue):
    #Check for 1 or 0
    if inValue <= 1:
        return False
    
    #Calculation
    for x in range(2, int(inValue**0.5)+1):
        print("The index is: "+ str(x) +" The number is "+ str(inValue)
              +" and the resulting modulus is: " + str(inValue%x))
        if inValue%x == 0:
            return False

    return True

#Output my Prime list
def output_prime_list(inList):
    print("\nYour list of prime numbers: ", inList)

#Closer
def closer():
    print("\nThank you for using my program.")

#Main
def main():
    header()
    
    output_prime_list(find_prime(my_range()))

    closer()

main()

#Hello Professor. Please read.
#Did I make appropriate functions? Any pointers on how I can better my code?
