####################################
#This is Brandon's lab 8 assignment#
#Lab 8: Piglatin translator        #
#Name: Brandon Lee                 #
#ACCeID: b2301435                  #
#Date: 6-21-23                     #
####################################

#Libraries
import sys

#Global Constants
VOWELS = ['A','a','E','e','I','i','O','o','U','u']
AY = "ay "
YAY = "yay "

#Header
def header():
    print("Here is my code for English/Piglatn translator\n\n")

#Display
def display():
    print("Please select one option:\n"
            "\t1 - English to Piglatin translation\n"
            "\t2 - Piglatin to Enlish translation\n"
            "\tx - Exit program\n")

#User English/Piglatin Input
def user_input():
    option = ""
    while option != 'x':
        display()
        option = input("Option: ")
        if option == '1':
            print("You have selected option", option, "\n")
            translate_to_piglatin()
        elif option == '2':
            print("You have selected option", option, "\n")
            translate_to_english()

#User Sentance Input
def user_sentence_input():
    isValid = False
    counter = 4
    while not(isValid):
        sentence = input("Input a sentence.\n"
                         "Sentence: ")
        if sentence.replace(" ", "").replace(".","").isalpha():
            isValid = True
            print("Your sentence is:", sentence, "\n")
        else:
            counter -= 1
            if counter == 0:
                print("Max tries reached")
                closer()
                sys.exit()
            print("You have entered an invalid input.\n"
                  "You have", counter, "tries left")
    return sentence

#Translate to English Function
def translate_to_english():
    sentence = user_sentence_input()
    words = sentence.split()
    #remove period
    if words[-1].endswith("."):
        words[-1] = words[-1].replace(".","")

    engWords = []
    for word in words:
        if word.endswith(YAY.strip()):
            engWord = word.replace(YAY.strip(), " ")
        else:
            engWord = word.replace(AY.strip(), "")
            engWord = engWord[-1]+engWord[0:len(engWord)-1]
            engWord = engWord + " "
        engWords.append(engWord)
    engSentence = ""
    engSentence = engSentence.join(engWords).strip()
    print("Translation:", engSentence.lower() + "\n")

#Translate to Piglatin Function
def translate_to_piglatin():
    sentence = user_sentence_input()
    words = sentence.split()
    #remove period
    if words[-1].endswith("."):
        words[-1] = words[-1].replace(".","")
        
    pigWords = []
    for word in words:
        if word[0] in VOWELS:
            pigWord = word + YAY
        else:
            pigWord = word[1:len(word)] + word[0] + AY
        pigWords.append(pigWord)
    pigSentence = ""
    pigSentence = pigSentence.join(pigWords).strip()
    print("Translation:", pigSentence.lower() + "\n")

#Closer
def closer():
    print("\n\nEnd of program. Goodbye.")

#Main Function
def main():
    header()
    user_input()
    closer()
    
main()
