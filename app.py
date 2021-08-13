#Brandon's Calculator

#input first variable
firstVar = input("Enter first variable: ")
firstVar = float(firstVar)

#input arithmetic
arith = input("Enter arithmetic(+,-,*,/): ")

#input second variable
secondVar = input("Enter second variable: ")
secondVar = float(secondVar)

#find ascii value of arithmatic
asciiArith = ord(arith)

equ = 0.0
if asciiArith == 43:
    equ = firstVar + secondVar
    print(equ)
elif asciiArith == 45:
    equ = firstVar - secondVar
    print(equ)
elif asciiArith == 42:
    equ = firstVar * secondVar
    print(equ)
elif asciiArith == 47:
    if secondVar == 0:
        print("Calculator go brrrrrr")
    else:
        equ = firstVar/SecondVar
        print(equ)





