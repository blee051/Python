#This is Brandon's Lab 3 Assignment
#Lab 3: The Flower Box
#Name: Brandon Lee
#ACCeID: b2301435
#Date: 6-11-23

#Libraries
import sys

#Flag variable
hasColor1 = False
hasColor2 = False

#Sentinal variable
counter = 5

#Heading
print("WELCOME TO THE FLOWER BOX! \n")

#Input & Error Check
#First Color
color1 = "color"
while hasColor1 == False:
    color1 = input("Enter a primary color: red, blue, yellow. q to quit: ").lower()
    if color1 == "red" or color1 == "blue" or color1 == "yellow":
        hasColor1 = True
    elif color1 == 'q':
        print("End of program")
        sys.exit()
    else:
        counter -= 1
        if counter == 0:
            print("User has reached the maximum amount of tries.")
            print("Restart the program and try again.")
            sys.exit()          
        print("Invaled input. You have", counter, "tries left.")

print("You have selected", color1, "as first primary color.")

#Second Color
counter = 5
color2 = "color"
while hasColor2 == False:
    color2 = input("Enter a primary color: red, blue, yellow. 'q' to quit: ").lower()
    if color2 == "red" or color2 == "blue" or color2 == "yellow":
        hasColor2 = True
    elif color2 == 'q':
        print("End of program")
        sys.exit()
    else:
        counter -= 1
        if counter == 0:
            print("User has reached the maximum amount of tries.")
            print("Restart the program and try again.")
            sys.exit()
        print("Invaled input. You have", counter, "tries left.")

print("You have selected", color2, "as second primary color.")

#Output
print("When you mix,", color1, "and", color2, "you get:") 
if color1 == "red" and color2 == "red":
    print("Red")
elif color1 == "red" and color2 == "blue":
    print("Purple")
elif color1 == "red" and color2 == "yellow":
    print("Orange")
elif color1 == "blue" and color2 == "red":
    print("Purple")
elif color1 == "blue" and color2 == "blue":
    print("Blue")
elif color1 == "blue" and color2 == "yellow":
    print("Green")
elif color1 == "yellow" and color2 == "red":
    print("Orange")
elif color1 == "yellow" and color2 == "blue":
    print("Green")
else:
    print("Yellow")

#Close
print("\nThank you for using the Flower Box. End of program.")

#PROFESSOR - PLEASE READ
#This will be posted to my github. Please provide any feedback on how I can improve my code.
#Please introduce any concepts not mentioned in class, if possible. It would be of great resource.
#What would a employer want from my code?
#Thank you.
