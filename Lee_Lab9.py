####################################
#This is Brandon's lab 9 assignment#
#Lab 9: Dictionary                 #
#Name: Brandon Lee                 #
#ACCeID: b2301435                  #
#Date: 6-28-23                     #
####################################

#header
def header():
    print("This is my Dictionary of classes program\n\n")

#Create first dictionary
def class_rooms():
    classRooms = { "CS101":"3004", "CS102":"4501", "CS103":"6755",
                   "NT110":"1244","CM241":"1411" }
    return classRooms

#Create second dictionary
def class_prof():
    classProfessors = { "CS101":"Haynes", "CS102":"Alvarado",
                        "CS103":"Rich", "NT110":"Burke", "CM241":"Lee" }
    return classProfessors

#Create third dictionary
def class_time():
    classTime = { "CS101":"8:00am", "CS102":"9:00am", "CS103":"10:00am"
                  , "NT110":"11:00am","CM241":"11:00pm" }
    return classTime

#Class list
def class_list():
    classList = ["CS101","CS102","CS103","NT110","CM241"]
    return classList

#User Input
def user_input():
    valInput = False
    while not(valInput):
        userInput = input("Enter a class name:")
        if userInput.upper() in class_list():
            valInput = True
            print("Class:"+userInput.upper()+
                  " Room:"+class_rooms()[userInput.upper()]+
                  " Instructor:"+class_prof()[userInput.upper()]+
                  " Time:"+class_time()[userInput.upper()])
        else:
            print("Incorrect input")

#Closer
def closer():
    print("\nEnd of program. Goodbye.")

#main
def main():
    header()
    user_input()
    closer()

main()
