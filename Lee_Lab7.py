####################################
#This is Brandon's lab 7 assignment#
#Lab 7: MLB World series           #
#Name: Brandon Lee                 #
#ACCeID: b2301435                  #
#Date: 6-21-23                     #
####################################

#Subo Code:
#Input: WorldSeriesWinners.txt file
#---Function: Open this file using read
#---function: Ask user for team name
#Calculation: Use a loop to compare name to each line. if name found,
#scan file and count the name
#Idea: create a 2D list where a list of repeating team names will stack,
#and those stacks will be in a list
#---function: search for team
#---function: add to counter
#Output:
#---Function: Output name and win count

#Library
import sys

#Header
def header():
    print("Welcome to the World Series Winners between 1903 and 2009!!\n\n")

#Open Input File
def open_text_file():
    try:
        file = r"C:\Users\leebr\Desktop\Python Files\temp\WorldSeriesWinners.txt"
        inputFile = open(file, 'r')
        return inputFile
    except IOError as e:
        print("An IOError occurred.", str(e))

#User input
def user_team_name(file):
    teamName = input("Name a MLB baseball team: ")
    counter = 4
    while not(does_name_exist(teamName, file)):
        counter -= 1
        if counter == 0:
            print("Max tries met. End of program.")
            sys.exit()
        print("This name,", teamName, ", does not exist. "
              "Please try again. You have", counter, "left.")
        teamName = input("Name a MLB baseball team: ")
        file.seek(0)
    return teamName

#Bool function: Does name exist in text file
def does_name_exist(name, file):
    file.seek(0)
    for line in file:
        if name == line.rstrip('\n'):
            return True
    return False

#Scan file
def scan_file(name, file):
    file.seek(0)
    counter = 0
    for line in file:
        if name == line.rstrip('\n'):
            counter+=1
    return counter

#Ouput wins and the team name
def output_funct(wins, name):
    print("\n\nTeam Name:", name, "\nWins:", wins)


#Close Input File
def close_text_file(file):
    try:
        file.close()
    except AttributeError:
        print("Invalid file object.")

#Closer
def closer():
    print("\n\nEnd of program. Goodbye.")

#Main
def main():
    header()
    #file open
    inputFile = open_text_file()
    #name
    userTeamName = user_team_name(inputFile)
    #wins
    wins = scan_file(userTeamName, inputFile)
    #output
    output_funct(wins, userTeamName)
    #file close
    close_text_file(inputFile)
    closer()

main()
