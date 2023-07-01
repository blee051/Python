#Here is my Lab2 Assignment
#Name: Brandon Lee
#ACCeID: b2301435
#Date: 6-6-23
#Lab Purpose: Calculate and Display total cost of produce including tax

#Fixed Value of Produce
applePrice = .75
pearPrice = .85
peachPrice = .95

#Fixed Value of Tax
tax = .0825

#Input Quantity of Produce
apples = input("Enter quantity of apples: ")
pears = input("Enter quantity of pears: ")
peaches = input("Enter quantity of pears: ")

#Convert Int to Float
apples = float(apples)
pears = float(pears)
peaches = float(peaches)

#Calculation: Price per Quantity
totalAppleCost = apples*applePrice
totalPearCost = pears*pearPrice
totalPeachCost = peaches*peachPrice

#Calculation: Tax Cost
totalTax = tax*(totalAppleCost+totalPearCost+totalPeachCost)

#Calculation: Total Cost
totalCost = totalTax + totalAppleCost + totalPearCost + totalPeachCost

#Print Produce Quantity Amount                
print("Apples:",apples, "Pears:",pears, "Peaches:",peaches)

#Print Produce Price per Quantity
print("Total Apple Cost: $"+str(f"{totalAppleCost:.2f}"))
print("Total Pear Cost: $"+str(f"{totalPearCost:.2f}"))
print("Total Peach Cost: $"+str(f"{totalPeachCost:.2f}"))

#Print Tax Cost
print("Total Tax Cost: $"+str(f"{totalTax:.2f}"))

#Print Total Cost
print("Total Cost: $"+str(f"{totalCost:.2f}"))
