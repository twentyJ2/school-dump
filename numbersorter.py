firstnum=float(input("This program sorts numbers from greatest to least, left to right.\nInput your first number: "))
seconnum=float(input("Input your second number: "))
thirdnum=float(input("Input your third number: "))
first=0.0
second=0.0
third=0.0
# Please welcome the ladder of terror.
if firstnum>seconnum:
    # otherwise second>=first
    if seconnum>=thirdnum:   #1 2 3
        first=firstnum
        second=seconnum
        third=thirdnum
    elif thirdnum>seconnum:  #1 3 2
        first=firstnum
        second=thirdnum
        third=seconnum
elif seconnum>thirdnum:
    if firstnum>=thirdnum:   #2 1 3
        first=seconnum
        second=firstnum
        third=thirdnum
    elif thirdnum>firstnum:  #2 3 1
        first=seconnum
        second=thirdnum
        third=firstnum  
else: #thirdnum is >= rest by this point
    if firstnum>seconnum:
        first=thirdnum
        second=firstnum
        third=seconnum
    else: #and can only be one result by now OR is all equal number.
        first=thirdnum
        second=seconnum
        third=firstnum
print(str(first),str(second),str(third))