#This is Brandon's Lab 4 Assignment
#Lab 4: Tuition Cost
#Name: Brandon Lee
#ACCeID: b2301435
#Date: 6-11-23

#Header
print("Here is the tuition cost for the next 5 years.\n")

#Constant Variables
TUITION = 8000.00
RATE = .03

#Output
print("The current tuition cost per semester is $" + format(TUITION, ',.2f') + ".")

#Year 1
tuitionInc = TUITION*RATE
total = TUITION + tuitionInc
print("In 1 year, the tuition per semester will be $"+\
      format(total, ',.2f') + ".")

#Years 2-5
for x in range(2, 6):
    tuitionInc = total*RATE
    total += tuitionInc
    print("In", str(x), "years, the tuition per semester will be $"+\
          format( total, ',.2f') + ".")

#PROFESSOR - PLEASE READ
#This will be posted to my github. Please provide any feedback on how I can improve my code.
#Please introduce any concepts not mentioned in class, if possible. It would be of great resource.
#What would a employer want from my code?
#Thank you.
