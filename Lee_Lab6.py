#This is Brandon's Lab 6 Assignment
#Lab 6: Input File
#Name: Brandon Lee
#ACCeID: b2301435
#Date: 6-13-23

#Header Function
def header():
    print("Here is a input file program.\n")

#Asking user input Function
def user_input():
    fileName = input("I need you to input a file name. e.g. numbers10.txt: ")
    return fileName

#Opening File Function
def open_file(fName):
    try:
        #Open path/!!!Using my personal directory. Here
        filePath = r'C:\Users\leebr\Desktop\Python Files\temp\\'


        #Create the file object
        inputFile = open(filePath+fName, 'r')
        print(inputFile)
        total = 0
        numAmount = 0
        for num1 in inputFile:
            print(num1)
            total+=int(num1)
            numAmount+=1

        #Calculation
        print("The total value is:", total)
        print("The amount of numbers:", numAmount)
        average = float(total/numAmount)
        print("Average:", average)
        inputFile.close()
    except OSError as e:
        print("An OSError occurred.", str(e))

    except IOError:
        print("An IOError occurred. File is not found or no permissions.")
    except ValueError:
        print("A ValueError occurred. Invalid input or incorrect format.")

#Closer Function
def closer():
    print("\nEnd of program. Goodbye.")

#Main Function
def main():
    header()
    open_file(user_input())
    closer()

main()
