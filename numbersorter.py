firstNum=float(input("This program sorts numbers from greatest to least, left to right.\nInput your firstPrint number: "))
secondNum=float(input("Input your secondPrint number: "))
thirdNum=float(input("Input your thirdPrint number: "))
firstPrint=0.0
secondPrint=0.0
thirdPrint=0.0
# Please welcome the ladder of terror.
if firstNum>secondNum:
    # otherwise secondPrint>=first
    if secondNum>=thirdNum:   #1 2 3
        firstPrint=firstNum
        secondPrint=secondNum
        thirdPrint=thirdNum
    elif thirdNum>secondNum:  #1 3 2
        firstPrint=firstNum
        secondPrint=thirdNum
        thirdPrint=secondNum
elif secondNum>thirdNum:
    if firstNum>=thirdNum:   #2 1 3
        firstPrint=secondNum
        secondPrint=firstNum
        thirdPrint=thirdNum
    elif thirdNum>firstNum:  #2 3 1
        firstPrint=secondNum
        secondPrint=thirdNum
        thirdPrint=firstNum  
else: #thirdNum is >= rest by this point
    if firstNum>secondNum:
        firstPrint=thirdNum
        secondPrint=firstNum
        thirdPrint=secondNum
    else: #and can only be one result by now OR is all equal number.
        firstPrint=thirdNum
        secondPrint=secondNum
        thirdPrint=firstNum
print(str(firstPrint),str(secondPrint),str(thirdPrint))